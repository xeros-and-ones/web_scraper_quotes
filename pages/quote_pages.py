from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from locators.quote_page_locators import QuotesPageLocator
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        # locator = QuotesPageLocator.QUOTE
        quote_tags = self.browser.find_elements(
            By.CSS_SELECTOR, QuotesPageLocator.QUOTE
        )
        return [QuoteParser(e) for e in quote_tags]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotesPageLocator.AUTHOR_DROPDOWN
        )
        return Select(element)

    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotesPageLocator.TAG_DROPDOWN
        )
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotesPageLocator.SEARCH_PUSH)

    def author_select(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def tag_select(self, tag: str):
        self.tags_dropdown.select_by_visible_text(tag)

    def get_author_quotes(self, author, tag) -> List[QuoteParser]:
        self.author_select(author)

        try:
            self.tag_select(tag)
        except NoSuchElementException:
            print("The Tag you entered doesn't exist")

        self.search_button.click()
        return self.quotes
