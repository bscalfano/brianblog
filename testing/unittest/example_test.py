from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = None

try:
    browser = webdriver.Chrome()
    browser.get("http://www.python.org")
    assert "Python" in browser.title
    searchBox = browser.find_element_by_name("q")
    searchBox.clear()
    searchBox.send_keys("pycon")
    searchBox.send_keys(Keys.RETURN)
    assert "No results found." not in browser.page_source
    print("Test Passed")
    sleep(5)

finally:
    if browser:
        browser.close()