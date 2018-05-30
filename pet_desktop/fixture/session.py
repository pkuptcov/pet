from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # Авторизация
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_id("mainPetrovichLogin_login").send_keys(username)
        wd.find_element_by_id("mainPetrovichLogin_password").send_keys(password)
        wd.find_element_by_css_selector("div.form_row [type=submit]").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "auth_user_link")))

    def logout(self):
        # Выход из ЛК
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_css_selector("a.auth_user_link").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Выход")))
        wd.find_element_by_link_text("Выход").click()