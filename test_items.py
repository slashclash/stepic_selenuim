import time
from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def is_element_present(browser):
    try:
        browser.find_element_by_css_selector("buttonbtn-add-to-basket")
        return True
    except NoSuchElementException:
        return False


def test_bucket_button(browser):
    browser.get(link)
    time.sleep(5)
    assert is_element_present(browser), "Button not found"
