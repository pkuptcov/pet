# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class ComplaintHelperControls:

    # Форма в СПК
    firstName = (By.NAME, "name")
    lastName = (By.NAME, "lastName")
    secondName = (By.NAME, "secondName")
    phone = (By.NAME, "phone")
    email = (By.NAME, "email")
    cardNumber = (By.NAME, "cardNumber")
    orderNumber = (By.NAME, "orderNumber")
    complaintDescription = (By.NAME, "complaintDescription")
    requirement = (By.NAME, "requirement")
    file = (By.NAME, "file[]")
    recaptcha = (By.XPATH, "//input[@type='file']")
    submit = (By.XPATH, "//input[@type='submit']")