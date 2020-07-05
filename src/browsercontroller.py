from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BrowserController:
    def __init__(self, driverpath):
        # self.browser = None
        # self.wait = None
        self.driver_path = driverpath
        self.browser = webdriver.Chrome(executable_path=self.driver_path)
        self.wait = WebDriverWait(self.browser, 3)
        print("INFO : Browser opened in constructor")

    def browser_open(self):
        """
        TODO : Fill docstrings
        """
        # self.browser = webdriver.Chrome(executable_path=self.driver_path)
        # self.wait = WebDriverWait(self.browser, 3)
        print("INFO : Browser opened")

    def browser_close(self):
        """
        TODO : Fill docstrings
        """
        self.browser.close()
        print("INFO : Browser closed")

    def load_and_get(self, url):
        self.browser.get(url)

    def get_element_text_by_xpath(self, xpath):
        try:
            text = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text.strip()
            return text
        except Exception as ex:
            print("EXCEPTION: Something bad happened. Perhaps no more element or timeout. Continuing")
        return ""
