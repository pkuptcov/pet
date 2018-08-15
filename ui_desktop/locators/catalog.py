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
    catalogSortPrice = (By.XPATH, "//span[@class='product_table_sorting_link sorting__link price price_asc active__link']")
    catalogSortTitle = (By.XPATH, "//span[@class='product_table_sorting_link sorting__link title title_asc']")

    # Вид отображение товара сеткой / списком
    catalogViewList = (By.CSS_SELECTOR, "ic_table")
    catalogViewTile = (By.CSS_SELECTOR, "ic_tile")

    # Выбор кол-ва товара
    catalogProductQuantityUp = (By.XPATH, "//span[@class='count--up product__stepper up unit--step']")
    catalogProductQuantityDown = (By.XPATH, "//span[@class='count--down product__stepper down unit--step']")
    catalogProductQuantityInput = (By.XPATH, "//div[@class='unit--input']")

    # Альтернативные единицы измерения
    catalogAlterM2 = (By.XPATH, "//p[contains(text(),'м2')]")
    catalogAlterMLinear = (By.XPATH, "//p[contains(text(),'метр погонный')]")
    catalogAlterM3 = (By.XPATH, "//p[contains(text(),'м3')]")
    catalogAlterPiece = (By.XPATH, "//p[contains(text(),'штуку')]")

    # Наличие
    catalogAvailability = (By.XPATH, "//span[@class='product_status ng-scope']")

    # Кнопка добавления в корзину
    catalogAddToCart = (By.XPATH, "//div[@class='btn_cart listing__product-button product__button ng-scope']")

    # Добавить к сравнению
    catalogProductCompare = (By.XPATH, "//div[contains(@class,'listing__product-compare compare__product')]")

