"""
TODO : Fill docstrings
"""
class Hashtag:
    """
    TODO : Fill docstrings
    """
    def __init__(self, seed, base, limit, related_tags_limit):
        self.seed_tag = seed
        self.base_url = base
        self.limit = limit
        self.related_tags_limit = related_tags_limit

    def get_hashtags(self, browser):
        """
        TODO : Fill docstrings
        """
        tags = []
        for i in range(1, self.related_tags_limit):
            xpath = '/html/body/div[1]/section/main/header/div[2]/div[2]/span/span[2]/div[{:d}]/a'.format(i)
            text = browser.get_element_text_by_xpath(xpath)
            if text != "":
                tags.append(text)
        return tags

    def get_posts_for_hashtag(self, browser):
        """
        TODO : Fill docstrings
        """
        xpath = '//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span'
        text = browser.get_element_text_by_xpath(xpath)
        posts = 0;
        if text != "" and text != " ":
            posts = int(text.replace(",", "").strip())
        return posts

    def merge_lists(self, list1, list2):
        """
        TODO : Fill docstrings
        """
        for items in list2:
            if items not in list1:
                list1.append(items)
        return list1

    def scrapping_loop(self, browser):
        """
        TODO : Fill docstrings
        """
        visited = []
        not_visited = [self.seed_tag]
        database = dict()
        numbers = 0
        while numbers < self.limit and len(not_visited) > 0:
            # Get next target hashtag from not visited list
            next_tag = not_visited[0]
            del not_visited[0]

            # Continue with next iteration if already visited
            if next_tag in visited:
                continue

            # Build url from base_url
            tag_url = self.base_url + next_tag.replace("#", "").strip()
            browser.load_and_get(tag_url)

            # Get number of post for this hashtag
            posts = self.get_posts_for_hashtag(browser)
            if posts <= 0:
                print("WARNING : Could not find any post for tag {:s}".format(next_tag))
                continue

            # Move hashtag to visited list. Add posts in dictionary. Increase counter
            visited.append(next_tag)
            database[next_tag] = posts
            numbers = numbers + 1

            # Get related hashtags
            related_hashtag_list = self.get_hashtags(browser)
            not_visited = self.merge_lists(not_visited, related_hashtag_list)

            print('INFO : Collected: {}'.format(next_tag))

        return database
