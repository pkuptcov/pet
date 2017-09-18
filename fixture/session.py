class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_id("mainPetrovichLogin_login").send_keys(username)
        wd.find_element_by_name("mainPetrovichLogin_password").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_css_selector("div.form_row [type=submit]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.auth_user_link").click()
        wd.find_element_by_link_text("Выход").click()