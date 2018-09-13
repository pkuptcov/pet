# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CatalogControls:

    # Каталог на главной странице
    catalogRoofingMaterialMain = (By.XPATH, "//span[(text()='Кровля, сайдинг, водосточные системы')]")

    # Категория 1 уровня
    catalogRoofingMaterialLevel1 = (By.XPATH, "//span[(text()='Кровельные материалы')]")

    # Категория 2 уровня
    catalogRoofingMaterialLevel2 = (By.XPATH, "//span[(text()='Ондулин')]")

    # Категория 3 уровня
    catalogRoofingMaterialLevel3 = (By.XPATH, "//span[(text()='Комплектующие для ондулина')]")

    # Сортировка по цене и по названию
    catalogSortDefault = (By.XPATH, "//p[(text()='по умолчанию')]")
    catalogSortPriceAsc = (By.XPATH, "//p[(text()='дешевое сверху')]")
    catalogSortPriceDesc = (By.XPATH, "//p[(text()='дорогое сверху')]")
    catalogSortTitleAsc = (By.XPATH, "//span[(text()='Я снизу')]")
    catalogSortTitleDesc = (By.XPATH, "//span[(text()='Я снизу')]")

    # Вид отображение товара сеткой / списком
    catalogViewListImage = (By.XPATH, "//a[@id='stnd']")
    catalogViewList = (By.XPATH, "//a[@id='line']")
    catalogViewBlock = (By.XPATH, "//a[@id='block']")

    # Выбор кол-ва товара
    catalogProductQuantityUp = (By.XPATH, "//span[@class='plus']")
    catalogProductQuantityDown = (By.XPATH, "//span[@class='minus']")
    catalogProductQuantityInput = (By.XPATH, "//input[@value='1']")

    # Наличие
    catalogAvailability = (By.XPATH, "//a[(text()='Есть в строительном центре')]")
    catalogAvailabilityClose = (By.XPATH, "//span[@class='close_mod']")

    # Кнопка добавления в корзину
    catalogAddToCart = (By.XPATH, "//button[@id='to_basket_button']")

    # Кнопка "Уже в козине"
    catalogAlreadyInCart = (By.XPATH, "//span[(text()='Уже в корзине')]")

    # Название товара
    catalogProductName = (By.XPATH, "//a[(text()='Гвоздь Ондулин  коричневый')]")

    # Фото товара
    catalogProductImage = (By.XPATH, "//img[(@alt='Гвоздь Ондулин  коричневый')]")
