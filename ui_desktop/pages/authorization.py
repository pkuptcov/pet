from ui_desktop.pages.base import BasePage
from ui_desktop.locators.auth_form import RegisterControls
from ui_desktop.locators.auth_form import AuthorizationControls
from ui_desktop.locators.auth_form import ForgotPasswordControls


class AuthorizationPage(BasePage):

    auth_controls = AuthorizationControls

    def login(self, username, password):
        self.input(*self.auth_controls.authLogin)(username)
        self.input(*self.auth_controls.authPassword)(password)
        self.click(*self.auth_controls.authForgotPasswordLink)
        self.click(*self.auth_controls.authRemember)
        self.click(*self.auth_controls.authSubmitButton)


class RegisterPage(BasePage):

    register_controls = RegisterControls

    def registration(self, firstname, lastname, email, password, kkd):
        self.input(*self.register_controls.registrationFirstname)(firstname)
        self.input(*self.register_controls.registrationLastname)(lastname)
        self.input(*self.register_controls.registrationEmail)(email)
        self.input(*self.register_controls.registrationPassword)(password)
        self.input(*self.register_controls.registrationCard)(kkd)
        self.click(*self.register_controls.registrationCaptcha)
        self.click(*self.register_controls.registrationNews)
        self.click(*self.register_controls.registrationSubmitButton)


class ForgotPasswordPage(BasePage):

    forgot_password_controls = ForgotPasswordControls

    def forgot_password(self):
        self.input(*self.forgot_password_controls.getPasswordEmail)
        self.input(*self.forgot_password_controls.getPasswordSubmit)
        self.click(*self.forgot_password_controls.getPasswordAuthLink)
        self.click(*self.forgot_password_controls.getPasswordClose)
