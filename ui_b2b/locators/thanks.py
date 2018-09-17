from selenium.webdriver.common.by import By


class ThanksControls:

    # Кнопки справа (Оплатить заказ, Сообщить об ошибке, Задать вопрос)
    thanksOrderLink = (By.XPATH, "//a[(text()='заказ')]")