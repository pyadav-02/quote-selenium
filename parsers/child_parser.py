from locators import ContentLocator
from selenium.webdriver.common.by import By

class QuoteContent:
    def __init__(self, quote):
        self.quote = quote

    @property
    def give_quote(self):
        return self.quote.find_element(By.CSS_SELECTOR, ContentLocator.QUOTE).text

    @property
    def give_author(self):
        return self.quote.find_element(By.CSS_SELECTOR, ContentLocator.AUTHOR).text

    @property
    def give_tags(self):
        tags = self.quote.find_elements(By.CSS_SELECTOR, ContentLocator.TAG)
        tags = [tag.text for tag in tags]
        return tags

    @property
    def give_contents(self):
        return {
            'name': self.give_quote,
            'author': self.give_author,
            'tags': self.give_tags
        }
