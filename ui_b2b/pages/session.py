from ui_b2b.pages.base import BasePage
from ui_b2b.locators.auth_form import AuthorizationControls
from ui_b2b.locators.left_menu import LeftMenuControls


class Session(BasePage):

    auth_controls = AuthorizationControls
    menu_controls = LeftMenuControls

    def login(self, username, password):

        # Авторизация
        self.input(*self.auth_controls.authLogin, value=username)
        self.input(*self.auth_controls.authPassword, value=password)
        self.click(*self.auth_controls.authSubmitButton)

    def logout(self):

        # Выход из ЛК
        self.click(*self.menu_controls.leftMenuLogout)