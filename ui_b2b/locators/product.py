from selenium.webdriver.common.by import By


class ProductController:

    # Добавить в корзину
    productAddToCart = (By.XPATH, "//div[@class='to-cart--button']")

    # Кнопка "Уже в козине"
    productAlreadyInCart = (By.XPATH, "//span[(text()='Уже в корзине')]")

    # Выбор кол-ва товара
    productQuantityUp = (By.XPATH, "//span[@class='plus']")
    productQuantityDown = (By.XPATH, "//span[@class='minus']")
    productQuantityInput = (By.XPATH, "//input[@value='1']")

    # Получить сертификат
    productGetCertificate = (By.XPATH, "//input[@value='Получить сертификат']")
    productGetCertificateOpen = (By.XPATH, "//a[(text()='— Ондулин_отказ_соотв')]")
    productGetCertificatePrint = (By.XPATH, "//a[(text()='Печать')]")
    productGetCertificateSave = (By.XPATH, "//a[(text()='Сохранить')]")
    productGetCertificateClose = (By.XPATH, "//span[@class='close_sert']")