from ui_desktop.pages.base import BasePage
from ui_desktop.locators.auth_form import RegisterControls
from ui_desktop.locators.auth_form import AuthorizationControls
from ui_desktop.locators.auth_form import ForgotPasswordControls


class AuthorizationPage(BasePage):

    auth_controls = AuthorizationControls

    def login_input(self, username):
        self.input(*self.auth_controls.authLogin)(username)

    def password_input(self, password):
        self.input(*self.auth_controls.authPassword)(password)

    def forgot_password_link(self):
        self.click(*self.auth_controls.authForgotPasswordLink)

    def remember_checkbox(self):
        self.click(*self.auth_controls.authRemember)

    def submit(self):
        self.click(*self.auth_controls.authSubmitButton)

    def close(self):
        self.click(*self.auth_controls.authClose)


class RegisterPage(BasePage):

    register_controls = RegisterControls

    def firstname_input(self):
        self.click(*self.register_controls.registrationFirstname)

    def lastname_input(self):
        self.click(*self.register_controls.registrationLastname)

    def email_input(self):
        self.click(*self.register_controls.registrationEmail)

    def password_input(self):
        self.click(*self.register_controls.registrationPassword)

    def card_input(self):
        self.click(*self.register_controls.registrationCard)

    def robot_checkbox(self):
        self.click(*self.register_controls.registrationCaptcha)

    def news_checkbox(self):
        self.click(*self.register_controls.registrationNews)

    def submit(self):
        self.click(*self.register_controls.registrationSubmitButton)

    def close(self):
        self.click(*self.register_controls.registrationClose)


class ForgotPasswordPage(BasePage):

    forgot_password_controls = ForgotPasswordControls

    def email_input(self):
        self.click(*self.forgot_password_controls.getPasswordEmail)

    def forgot_password_input(self):
        self.click(*self.forgot_password_controls.getPasswordSubmit)

    def auth_link(self):
        self.click(*self.forgot_password_controls.getPasswordAuthLink)

    def close(self):
        self.click(*self.forgot_password_controls.getPasswordClose)