from selenium.webdriver.common.by import By


class HeaderControls:

    # Форма выбора компании и города
    headerCompanyList = (By.XPATH, "//div[@class='organiztions_and-city-chosen-box js--slide-menu']")
    headerCompanyListSpb = (By.XPATH, "//div[(text()='Санкт-Петербург')]")

    # Корзина в шапке
    headerBasket = (By.XPATH, "//button[@class='basket_catalog_search']")
    headerBasketCount = (By.XPATH, "//p[@id='basket_val_number']")