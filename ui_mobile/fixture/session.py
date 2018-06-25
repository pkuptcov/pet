from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # Авторизация
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_css_selector("div.i--menu").click()
        if len(wd.find_elements_by_css_selector("div.user--name")) > 0:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.user--logout")))
            wd.find_element_by_css_selector("div.user--logout").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Вход")))
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_id("mainPetrovichLogin_login").send_keys(username)
        wd.find_element_by_id("mainPetrovichLogin_password").send_keys(password)
        wd.find_element_by_css_selector("button.ln--send").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//small[contains(text(),'Вы успешно вошли в аккаунт!')]")))

    def logout(self):
        # Выход из ЛК
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_css_selector("div.i--menu").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.user--logout")))
        wd.find_element_by_css_selector("div.user--logout").click()