from selenium.webdriver.common.by import By


class ProductController:

    # Наличие товара
    productAvailability = (By.XPATH, "//div[@class='goods--card']//p[(text()='Наличие')]")

    # Добавить в корзину
    productAddToCart = (By.XPATH, "//div[@class='goods--card']//button[@class='to--cart']")

    # Выбор кол-ва товара
    productQuantityUp = (By.XPATH, "//div[@class='goods--card']//div[@class='c--plus  c--stepper unit--step']")
    productQuantityDown = (By.XPATH, "//div[@class='goods--card']//div[@class='c--minus c--stepper unit--step']")
    productQuantityInput = (By.XPATH, "//div[@class='goods--card']//div[@class='cc--i unit--input']")

    # Альтернативные единицы измерения
    productAlterM2 = (By.XPATH, "//p[contains(text(),'м2')]")
    productAlterMLinear = (By.XPATH, "//p[contains(text(),'метр погонный')]")
    productAlterM3 = (By.XPATH, "//p[contains(text(),'м3')]")
    productAlterPiece = (By.XPATH, "//p[contains(text(),'штуку')]")

    # Детали, отзывы, вопросы
    productDetails = (By.XPATH, "//div[@class='tabs__choose']//h2[(text()='Детали')]")
    productReviews = (By.XPATH, "//div[@class='tabs__choose']//h2[(text()='Отзывы ')]")
    productQuestion = (By.XPATH, "//div[@class='tabs__choose']//h2[(text()='Вопросы ')]")
