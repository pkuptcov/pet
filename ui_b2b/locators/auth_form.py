# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class RegisterControls:

    # Форма регистрации
    registrationLastname = (By.XPATH, "//input[@id='lastName']")
    registrationFirstname = (By.XPATH, "//input[@id='firstName']")
    registrationCompany = (By.XPATH, " //input[@id='b2bUserCompany']")
    registrationInn = (By.XPATH, "//input[@id='b2bUserInn']")
    registrationEmail = (By.XPATH, "//input[@id='b2bUserEmail']")
    registrationPhone = (By.XPATH, "//input[@id='b2bUserPhone']")
    registrationAntibot = (By.XPATH, "//label[@for='antibot_check']")
    registrationSubmitButton = (By.XPATH, "//button[@class='registration_button_send']")


class AuthorizationControls:

    # Форма авторизации
    authLogin = (By.XPATH, "//input[@id='LoginInput']")
    authPassword = (By.XPATH, "//input[@id='PasswordInput']")
    authRemember = (By.XPATH, "//label[@for='no_exit_check']")
    authSubmitButton = (By.XPATH, "//button[@class='button_login_in']")
    authClose = (By.XPATH, "//a[@class='registration']")
    authForgotPasswordLink = (By.XPATH, "//a[contains(text(),'Не помню пароль')]")


class ForgotPasswordControls:

    # Форма восстановления пароля
    getPasswordEmail = (By.XPATH, "//input[@id='email']")
    getPasswordSubmit = (By.XPATH, "//span[(text()='Отправить')]")