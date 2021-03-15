from .base_page import BasePage
from .locators import ProductPageLocators
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_basket_button()
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        time.sleep(5)
        self.should_be_correct_names()
        self.should_be_correct_prices()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BACKET_BUTTON), "Add to basket button " \
                                                                                   "is not presented"

    def add_product_to_basket(self):
        add_to_bucket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BACKET_BUTTON)
        add_to_bucket_button.click()


    def should_be_correct_names(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        book_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_NAME)
        assert book_name.text == book_basket_name.text, "Names are not equal"

    def should_be_correct_prices(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        book_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE)
        assert book_price.text == book_basket_price.text, "Prices are not equal"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_not_be_success_message_after_basket(self):
        self.should_be_basket_button()
        self.add_product_to_basket()
        # self.solve_quiz_and_get_code()
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), \
            "Success message is presented, but should not be"



    def should_disappear_after_basket(self):
        self.should_be_basket_button()
        self.add_product_to_basket()
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD), \
            "Success message is not disappear, but should"