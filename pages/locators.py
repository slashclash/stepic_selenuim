from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LOGIN_FORM = (By.ID, "login_form")
    LOGIN_REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BACKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")

    MESSAGE_ADD = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_BASKET_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")