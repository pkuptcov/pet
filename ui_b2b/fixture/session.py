from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        # Авторизация
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_name("login").send_keys(login)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_class_name("button_login_in").click()
        wait.until(EC.element_to_be_clickable((By.NAME, "q")))

    def logout(self):
        # Выход из ЛК
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "exit_bg_icon")))
        wd.find_element_by_class_name("exit_bg_icon").click()