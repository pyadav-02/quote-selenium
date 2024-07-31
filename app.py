from selenium import webdriver
from parsers.parent_parser import Quote

edge = webdriver.Edge()
edge.get('https://quotes.toscrape.com/')
page = Quote(edge)

for quote in page.give_quotes:
    print(quote)

print('done')