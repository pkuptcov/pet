# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class RegisterHelperControls:
    registrationLink = (By.LINK_TEXT, "Регистрация")
    registrationFirstname = (By.ID, "mainPetrovichRegister_firstName")
    registrationLastname = (By.ID, "mainPetrovichRegister_lastName")
    registrationEmail = (By.ID, "mainPetrovichRegister_email")
    registrationPassword = (By.ID, "mainPetrovichRegister_password")
    registrationCard = (By.ID, "mainPetrovichRegister_card")
    registrationNews = (By.ID, "mainPetrovichRegister_checkbox")
    registrationSubmitButton = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")


class AuthorizationHelperControls:
    authLink = (By.LINK_TEXT, "Вход")
    authLogin = (By.ID, "mainPetrovichLogin_login")
    authPassword = (By.ID, "mainPetrovichLogin_password")
    authRemember = (By.NAME, "remember")
    authSubmitButton = (By.XPATH, "//button[contains(text(),'Вход')]")


class GetPasswordHelperControls:
    getPasswordLink = (By.LINK_TEXT, "Получить пароль")
    getPasswordEmail = (By.NAME, "email_restore")
    getPasswordSubmit = (By.XPATH, "//button[contains(text(),'Выслать')]")