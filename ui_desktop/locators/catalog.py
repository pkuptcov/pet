# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CatalogControls:

    # Каталог главный
    catalogMain = (By.XPATH, "//div[@class='catalog_dropdown-button']")

    # Ссылка на напольные покрытия
    catalogMainBuildingMaterial = (By.XPATH, "//p[contains(text(),'Напольные покрытия')]")

    # Ссылка на линолеум
    catalogFirstLevelLinoleum = (By.XPATH, "//a[@title='Перейти к каталогу: Линолеум']")

    # Ссылка на линолеум
    catalogSecondLevelLinoleum = (By.XPATH, "//a[@title='Перейти к каталогу: Линолеум полукоммерческий']")

    # Выбор по наличию в строительном центре
    catalogSubdivision = (By.XPATH, "//select[@id='subdivision-select']")
    catalogSubdivisionAll = (By.XPATH, "//option[@value='allBases']")
    catalogSubdivisionIndus = (By.XPATH, "//option[contains(text(),'Индустриальный')]")
    catalogSubdivisionMurmanka = (By.XPATH, "//option[contains(text(),'Мурманка')]")
    catalogSubdivisionParnas = (By.XPATH, "//option[contains(text(),'Парнас')]")
    catalogSubdivisionKadSever = (By.XPATH, "//option[contains(text(),'КАД Север')]")
    catalogSubdivisionPlanernaya = (By.XPATH, "//option[contains(text(),'Планерная')]")
    catalogSubdivisionSofiyskaya = (By.XPATH, "//option[contains(text(),'Софийская')]")
    catalogSubdivisionTallinskoe = (By.XPATH, "//option[contains(text(),'Таллинское')]")

    # Сортировка по цене и по названию
    catalogSortPrice = (By.XPATH, "//span[(text()='по цене')]")
    catalogSortTitle = (By.XPATH, "//span[(text()='по названию')]")
    catalogSortUsefulness = (By.XPATH, "//span[(text()='по полезности')]")
    catalogSortAccordance = (By.XPATH, "//span[(text()='по соответствию')]")

    # Вид отображение товара сеткой / списком
    catalogViewList = (By.CSS_SELECTOR, "ic_table")
    catalogViewTile = (By.CSS_SELECTOR, "ic_tile")

    # Выбор кол-ва товара
    catalogProductQuantityUp = (By.CSS_SELECTOR, "div.stepper-arrow.up.unit--step")
    catalogProductQuantityDown = (By.CSS_SELECTOR, "div.stepper-arrow.down.unit--step")
    catalogProductQuantityInput = (By.CSS_SELECTOR, "input.product__count")

    # Альтернативные единицы измерения
    catalogAlterM2 = (By.XPATH, "//p[contains(text(),'м2')]")
    catalogAlterMLinear = (By.XPATH, "//p[contains(text(),'метр погонный')]")
    catalogAlterM3 = (By.XPATH, "//p[contains(text(),'м3')]")
    catalogAlterPiece = (By.XPATH, "//p[contains(text(),'штуку')]")

    # Наличие
    catalogAvailability = (By.XPATH, "//span[@class='product_status ng-scope']")

    # Кнопка добавления в корзину
    catalogAddToCart = (By.XPATH, "//div[@class='btn_cart listing__product-button product__button ng-scope']")

    # Кнопка "В козине"
    catalogAlreadyInCart = (By.XPATH, "//span[(text()='в корзине')]")

    # Добавить к сравнению
    catalogProductCompare = (By.XPATH, "//div[contains(@class,'listing__product-compare compare__product')]")

    # Название товара
    catalogProductName = (By.CSS_SELECTOR, "a[data-product-code='101846']")

    # Фото товара
    catalogProductImage = (By.CSS_SELECTOR, "img[src='//tdp.ru/images/8e5a2946-b646-11df-9b7f-001f29c68b0a_220x220_1.tif']")
