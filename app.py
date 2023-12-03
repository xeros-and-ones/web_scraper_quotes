from selenium import webdriver

from pages.quote_pages import QuotesPage

chrome = webdriver.Chrome()
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)


author = input("enter the name of the author:\n--> ")
tag = input("enter the tag:\n--> ")


page.get_author_quotes(author, tag)

for quote in page.quotes:
    print(f"Quote: {quote.content}\n{quote.author}\n")
