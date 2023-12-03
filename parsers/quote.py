from locators.quote_locators import QuoteLocator
from selenium.webdriver.common.by import By


class QuoteParser:
    """
    takes in a single quote div and outputs the Content, Author and Tags
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"Quote: {self.content} \nBy: {self.author}\n"

    @property
    def content(self):
        locator = QuoteLocator.CONTENT
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def author(self):
        locator = QuoteLocator.AUTHOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def tags(self):
        locator = QuoteLocator.TAG
        return self.parent.find_elements(By.CSS_SELECTOR, locator)
