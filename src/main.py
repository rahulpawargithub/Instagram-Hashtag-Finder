from configparser import ConfigParser
from hashtag import Hashtag
from browsercontroller import BrowserController


def add_hash_symbol(tag_list):
    for i in range(len(tag_list)):
        tag = tag_list[i]
        if tag.find('#') == -1:
            tag = "#" + tag
        tag_list[i] = tag


def print_sorted_database(database):
    """
        TODO : Fill docstrings
        """
    print("INFO : Printing collected hashtags and volume")
    for key, value in sorted(database.items(), key=lambda item: item[1], reverse=True):
        print('\t {:20s} \t {:>10d} '.format(key, value))


def main():
    # Read config file
    parser = ConfigParser()
    parser.read('../config.ini')

    sections = ["Default", "Seeds"]
    driver_path = parser.get(sections[0], "driverpath")
    baseurl = parser.get(sections[0], "baseurl")
    num_tags = parser.get(sections[0], "numtags")
    related_tag_limit = parser.get(sections[0], "relatedtaglimit")
    num_seeds = parser.get(sections[0], "numseeds")

    # get seed hash tags
    seeds = []
    for i in range(int(num_seeds)):
        seeds.append(parser.get(sections[1], "seed{:d}".format(i + 1)))
    add_hash_symbol(seeds)

    # browser object and hashtag objects
    browser = BrowserController(driver_path)
    browser.browser_open()
    database = dict()
    for seed in seeds:
        hashtags = Hashtag(seed, baseurl, int(num_tags), int(related_tag_limit))
        database.update(hashtags.scrapping_loop(browser))
    browser.browser_close()

    # Print collected hashtags
    print_sorted_database(database)


if __name__ == "__main__":
    main()
