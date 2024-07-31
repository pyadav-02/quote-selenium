from locators import QuoteLocator
from parsers.child_parser import QuoteContent
from selenium.webdriver.common.by import By

class Quote:
    def __init__(self, page):
        page = page.find_elements(By.CSS_SELECTOR, QuoteLocator.QUOTE_SECTION)
        self.page = page

    @property
    def give_quotes(self):
        quotes = []
        for quote in self.page:
            quote = QuoteContent(quote)
            quotes.append(quote.give_contents)
        return quotes
