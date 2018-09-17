# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class RegisterControls:

    # Форма регистрации
    registrationFirstname = (By.ID, "mainPetrovichRegister_firstName")
    registrationLastname = (By.ID, "mainPetrovichRegister_lastName")
    registrationEmail = (By.ID, "mainPetrovichRegister_email")
    registrationPassword = (By.ID, "mainPetrovichRegister_password")
    registrationCard = (By.ID, "mainPetrovichRegister_card")
    registrationCaptcha = (By.CSS_SELECTOR, "recaptcha-checkbox-checkmark")
    registrationNews = (By.ID, "mainPetrovichRegister_checkbox")
    registrationSubmitButton = (By.XPATH, "//button[(text()='Зарегистрироваться')]")


class AuthorizationControls:

    # Форма авторизации
    authLogin = (By.ID, "mainPetrovichLogin_login")
    authPassword = (By.ID, "mainPetrovichLogin_password")
    authForgotPasswordLink = (By.LINK_TEXT, "//span[@class='ln--forgot']")
    authSubmitButton = (By.XPATH, "//button[(text()='Вход')]")
    authRemember = (By.XPATH, "//span[(text()='Запомнить меня')]")


class ForgotPasswordControls:

    # Форма восстановления пароля
    getPasswordEmail = (By.NAME, "email_restore")
    getPasswordSubmit = (By.XPATH, "//button[(text()='Выслать')]")
    getPasswordClose = (By.XPATH, "//span[@id='closeForm']")