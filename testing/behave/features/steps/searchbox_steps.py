from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


@given(u'we have a browser looking at python.org')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://www.python.org")




@when(u'we search for "{target}" using "{name}"')
def step_impl(context, target, name):
    search_box = context.browser.find_element_by_name("q")
    search_box.clear()
    search_box.send_keys(target)
    search_box.send_keys(Keys.RETURN)
#   raise NotImplementedError(u'STEP: When we search for "lasdjfghklhfdkj"')


@then(u'we get a "No Results" message')
def step_impl(context):
    assert "No results found." in browser.page_source  
#   raise NotImplementedError(u'STEP: Then we get a "No Results" message')


@then(u'we don\'t get a "No Results" message')
def step_impl(context):
    assert "No results found." not in browser.page_source