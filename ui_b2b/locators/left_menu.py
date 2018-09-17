# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LeftMenuControls:

    # Левое меню
    leftMenuCatalog = (By.XPATH, "//a[@href='/catalog/']//li")
    leftMenuOrders = (By.XPATH, "//a[@href='/orders/']//li")
    leftMenuCart = (By.XPATH, "//a[@href='/cart/']//li")
    leftMenuCalculate = (By.XPATH, "//a[@href='/calculate/']//li")
    leftMenuNotes = (By.XPATH, "//a[@href='/notes/']//li")
    leftMenuProfile = (By.XPATH, "//a[@href='/profile/']//li")
    leftMenuLogout = (By.XPATH, "//a[@href='/logout/']//li")

    # Написать менеджеру
    leftMenuWriteToManagerInput = (By.XPATH, "//textarea[@id='chat_message']")
    leftMenuWriteToManagerSubmit = (By.XPATH, "//span[(text()='Отправить')]")
    leftMenuRetyrnToMainMenu = (By.XPATH, "//span[(text()='Основное меню')]")