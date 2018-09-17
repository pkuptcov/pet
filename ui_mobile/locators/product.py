from selenium.webdriver.common.by import By


class ProductController:

    # Увеличить фото
    productPhotoEnlarge = (By.XPATH, "//button[@title='Увеличить']")

    # Добавить в корзину
    productAddToCart = (By.XPATH, "//div[@class='to-cart--button']")

    # Добавить к сравнению
    productAddToCompare = (By.XPATH, "//div[@class='product--compare compare__product']")

    # Добавить к сравнению
    productAddToEstimate = (By.XPATH, "//div[@class='product--toestimate toestimate__product']")

    # Выбор кол-ва товара
    catalogProductQuantityUp = (By.XPATH, "//span[@class='count--up product__stepper up unit--step']")
    catalogProductQuantityDown = (By.XPATH, "//span[@class='count--down product__stepper down unit--step']")
    catalogProductQuantityInput = (By.XPATH, "//div[@class='to-cart--count']//input[@value='1']")

    # Альтернативные единицы измерения
    catalogAlterM2 = (By.XPATH, "//p[contains(text(),'м2')]")
    catalogAlterMLinear = (By.XPATH, "//p[contains(text(),'метр погонный')]")
    catalogAlterM3 = (By.XPATH, "//p[contains(text(),'м3')]")
    catalogAlterPiece = (By.XPATH, "//p[contains(text(),'штуку')]")

    # Документация
    catalogDocument = (By.XPATH, "//div[@class='docs--item modal--area']//div[@class='docs--preview modal--docs']")
    catalogcatalogDocumentPrint = (By.XPATH, "//a[@class='helper--print']")
    catalogcatalogDocumentDownload = (By.XPATH, "//a[@class='helper--download']")

    # Сертификаты
    catalogCertificate = (By.XPATH, "//div[@class='docs--item']//div[@class='docs--preview modal--docs']")
    catalogCertificatePrint = (By.XPATH, "//a[@class='helper--print']")
    catalogCertificateDownload = (By.XPATH, "//a[@class='helper--download']")