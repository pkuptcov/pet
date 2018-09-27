from ui_mobile.pages.base import BasePage
from ui_mobile.locators.auth_form import AuthorizationControls
from ui_mobile.locators.header import HeaderControls


class Session(BasePage):

    auth_controls = AuthorizationControls
    header_controls = HeaderControls

    def login(self, username, password):

        # Авторизация
        self.click(*self.header_controls.leftMenu)
        if len(self.wd.find_elements(*self.header_controls.menuCabinetUsername)) > 0:
            self.click(*self.header_controls.menuCabinetLogout)
            self.click(*self.header_controls.leftMenu)
        self.click(*self.header_controls.menuCabinetAuth)
        self.input(*self.auth_controls.authLogin, value=username)
        self.input(*self.auth_controls.authPassword, value=password)
        self.click(*self.auth_controls.authSubmitButton)

    def logout(self):

        # Выход из ЛК
        self.click(*self.header_controls.leftMenu)
        self.click(*self.header_controls.menuCabinetLogout)