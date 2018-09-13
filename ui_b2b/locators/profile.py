# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class ProfileControls:

    # Профиль
    profileEdit = (By.XPATH, "//a[@href='/prof_edit/']")
    profileAdd = (By.XPATH, "//div[@class='edit_profile others']//a[@href='#']")
    profileCompany = (By.XPATH, "//div[@class='profile_others_info']//p")


class ProfileEditControls:

    # Редактирование профиля
    profileEditLastname = (By.XPATH, "//input[@name='lastName']")
    profileEditFirstname = (By.XPATH, "//input[@name='firstName']")
    profileEditMiddlename = (By.XPATH, "//input[@name='middleName']")
    profileEditEmail = (By.XPATH, "//input[@name='email']")
    profileEditPhone = (By.XPATH, "//input[@name='phone']")
    profileEditLogin = (By.XPATH, "//input[@class='login']")

    profileEditPasswordOld = (By.XPATH, "//input[@name='passwordOld']")
    profileEditPasswordNew = (By.XPATH, "//input[@name='passwordNew']")
    profileEditPasswordConfirm = (By.XPATH, "//input[@name='passwordConfirm']")

    profileEditBack = (By.XPATH, "//div[@class='save_changes']//a[@class='back_no_save']")
    profileEditSubmit = (By.XPATH, "//button[@type='submit']")


class ProfileAddControls:

    # Добавить контрагента
    profileAddCompany = (By.XPATH, "//input[@name='inn']")
    profileAddCompanySubmit = (By.XPATH, "//span[(text()='Добавить покупателя')]")
    profileAddCompanyClose = (By.XPATH, "//span[@class='close_new_buyer']")