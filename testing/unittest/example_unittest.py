from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import unittest

class SearchBox_TestCase(unittest.TestCase):

    def test_000_no_results(self):
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
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)

# try:
#     driver = webdriver.Chrome()
#     driver.get("http://www.python.org")
#     assert "Python" in driver.title
#     searchBox = driver.find_element_by_name("q")
#     searchBox.clear()
#     searchBox.send_keys("pycon")
#     searchBox.send_keys(Keys.RETURN)
#     assert "No results found." not in browser.page_source
#     print("Test Passed")
#     sleep(5)
    
# finally:
#     if driver:
#         driver.close()