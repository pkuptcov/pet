from ui_desktop.pages.base import BasePage
from ui_desktop.locators.auth_form import AuthorizationHelperControls
from ui_desktop.locators.header import HeaderControls


class Session(BasePage):

    auth_controls = AuthorizationHelperControls
    header_controls = HeaderControls

    def login(self, username, password):
        # Авторизация

        if len(*self.header_controls.authLink) > 0:
            self.click(*self.header_controls.headerUsername)
            self.click(*self.header_controls.headerLogout)
            self.click(*self.header_controls.authLink)
        self.input(*self.auth_controls.authLogin)(username)
        self.input(*self.auth_controls.authPassword)(password)
        self.click(*self.auth_controls.authSubmitButton)

    def logout(self):

        # Выход из ЛК
        self.click(*self.header_controls.headerUsername)
        self.click(*self.header_controls.headerLogout)