import time


class RegisterHelper:

    def __init__(self, app):
        self.app = app

    def register(self, firstname, email, password):
        # Регистрация
        wd = self.app.wd
        wd.find_element_by_link_text("Регистрация").click()
        wd.find_element_by_id("mainPetrovichRegister_firstName").send_keys(firstname)
        wd.find_element_by_id("mainPetrovichRegister_email").send_keys(email)
        wd.find_element_by_id("mainPetrovichRegister_password").send_keys(password)
        wd.find_element_by_id("mainPetrovichRegister_checkbox").click()
        wd.find_element_by_xpath("//button[contains(text(),'Зарегистрироваться')]").click()
        time.sleep(1)