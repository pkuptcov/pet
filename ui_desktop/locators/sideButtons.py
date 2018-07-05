# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class SideButtonsHelperControls:
    # Кнопки справа (Оплатить заказ, Сообщить об ошибке, Задать вопрос)
    sideButtonOrder = (By.CSS_SELECTOR, ".side_button_order")
    sideButtonError = (By.CSS_SELECTOR, ".side_button_error")
    sideButtonQuestion = (By.CSS_SELECTOR, ".side_button_question")