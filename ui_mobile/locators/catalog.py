# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CatalogControls:

    # Каталог главный
    catalogDropown = (By.XPATH, "//div[@class='l--top-catalog']//div[@class='i--catalog']")

    # Ссылка на напольные покрытия
    catalogMainBuildingMaterial = (By.XPATH, "//div[@class='f--catalog']//span[(text()='Напольные покрытия')]")

    # Ссылка на линолеум
    catalogFirstLevelLinoleum = (By.XPATH, "//div[@class='category--info']//p[(text()='Линолеум')]")

    # Ссылка на линолеум
    catalogSecondLevelLinoleum = (By.XPATH, "//div[@class='category--block']//p[(text()='Линолеум полукоммерческий')]")

    # Сортировка по цене и по названию
    catalogSort = (By.XPATH, "//div[contains(@class,'sorting--choose')]")
    catalogSortPriceAsc = (By.XPATH, "//div[@class='sorting--order price--asc']//p[(text()='по цене')]")
    catalogSortPriceDesc = (By.XPATH, "//div[@class='sorting--order price--desc']//p[(text()='по цене')]")
    catalogSortTitleAsc = (By.XPATH, "//div[@class='sorting--order title--asc']//p[(text()='по названию')]")
    catalogSortTitleDesc = (By.XPATH, "//div[@class='sorting--order price--desc']//p[(text()='по названию')]")

    # Выбор кол-ва товара
    catalogProductQuantityDown = (By.XPATH, "(//div[@class='c--minus c--stepper unit--step'])[1]")
    catalogProductQuantityUp = (By.XPATH, "(//div[@class='c--plus  c--stepper unit--step'])[1]")
    catalogProductQuantityInput = (By.XPATH, "(//div[@class='c--input'])[1]")

    # Альтернативные единицы измерения
    catalogAlterM2 = (By.XPATH, "(//p[(text()='За м2')])[1]")
    catalogAlterMLinear = (By.XPATH, "(//p[(text()='за метр погонный')])[1]")
    catalogAlterM3 = (By.XPATH, "(//p[(text()='За м3')])[1]")
    catalogAlterPiece = (By.XPATH, "(//p[(text()='за штуку')])[1]")
    catalogAlterPack = (By.XPATH, "(//p[(text()='за упаковку')])[1]")

    # Кнопка добавления в корзину
    catalogAddToCart = (By.XPATH, "(//button[(text()=' В корзину ')])[1]")

    # Кнопка "В козине"
    catalogAlreadyInCart = (By.XPATH, "(//button[(text()='В корзине')])[1]")

    # Название товара
    catalogProductName = (By.XPATH, "(//div[@class='title--i'])[1]")

    # Фото товара
    catalogProductImage = (By.XPATH, "(//a[@class='photo--link'])[1]")
