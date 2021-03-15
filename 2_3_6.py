from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:


    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(1)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text.split(" ")[-1]
    print(alert_text)
    alert.accept()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
