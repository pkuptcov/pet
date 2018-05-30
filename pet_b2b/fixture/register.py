from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RegisterHelper:

    def __init__(self, app):
        self.app = app

    def register(self, lastname, firstname, company, inn, email, phone):
        # Регистрация
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_class_name("registration").click()
        wd.find_element_by_name("lastName").send_keys(lastname)
        wd.find_element_by_name("firstName").send_keys(firstname)
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("inn").send_keys(inn)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("phone").send_keys(phone)
        wd.find_element_by_css_selector("label[for='antibot_check']").click()
        wd.find_element_by_css_selector("button.registration_button_send").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.head_basket_wrapper')))