from selenium.webdriver.common.by import By


class CalculateControls:

    # Работа с корзиной и товарами
    calculateStatement = (By.XPATH, "//span[(text()='Ведомость')]")
    calculateAct = (By.XPATH, "//span[(text()='Акты сверок')]")