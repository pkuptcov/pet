from selenium.webdriver.common.by import By


class OrderListControls:

    # Работа со списком заказов
    orderListInProgress = (By.XPATH, "//span[(text()='В работе')]")
    orderListDone = (By.XPATH, "//span[(text()='Выполненные')]")
    orderListAll = (By.XPATH, "//span[(text()='Все')]")

    # Поиск заказов
    orderSearchNumber = (By.XPATH, "//input[@id='orderSearch']")
    orderSearchDateFrom = (By.XPATH, "//input[@id='datepicker']")
    orderSearchDateTo = (By.XPATH, "//input[@id='datepicker_end']")
    orderSearchCalendarPrevMonth = (By.XPATH, "//a[@title='Prev']")
    orderSearchCalendarNextMonth = (By.XPATH, "//a[@title='Next']")
    orderSearchCalendarFirstDay = (By.XPATH, "//a[(text()='1')]")
    orderSearchSubmit = (By.XPATH, "//input[@id='sendSelForm']")
