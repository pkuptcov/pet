# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CabinetProfileHelperControls:

    # Левое меню в ЛК
    menuLinkProfile = (By.XPATH, "//a[@class='menu__link'][contains(text(),'Профиль')]")
    menuLinkProfileOld = (By.XPATH, "//a[contains(@class,'menu__link')][contains(text(),'Регистрационная информация')]")
    menuLinkCart = (By.XPATH, "//a[@class='menu__link'][contains(text(),'Корзина')]")
    menuLinkOrders = (By.XPATH, "//a[@class='menu__link'][contains(text(),'Заказы')]")
    menuLinkProjects = (By.XPATH, "//a[@class='menu__link'][contains(text(),'Проекты')]")
    menuLinkEstimates = (By.XPATH, "//a[@class='menu__link'][contains(text(),'Сметы')]")
    menuLinkExpense = (By.XPATH, "//a[@class='menu__link'][contains(text(),'Расходы')]")

    # Профиль
    profileFormFirstName = (By.CSS_SELECTOR, "input['formcontrolname=firstName']")
    profileFormLastName = (By.CSS_SELECTOR, "input['formcontrolname=lastName']")
    profileFormLogin = (By.CSS_SELECTOR, "input['formcontrolname=login']")
    profileFormEmail = (By.CSS_SELECTOR, "input['formcontrolname=email']")
    profileFormPassword = (By.CSS_SELECTOR, "input['formcontrolname=password']")
    profileFormPasswordConfirm = (By.CSS_SELECTOR, "input['formcontrolname=passwordConfirm']")
    profileFormSave = (By.CSS_SELECTOR, "div.pet_input__col")

    # Моя карта
    profileCardStatusLink = (By.XPATH, "//a[contains(text(),'Статусы карты клуба Петрович')]")
    profileCardNumber = (By.CSS_SELECTOR, "input['formcontrolname=number']")
    profileCardNumberSubmit = (By.XPATH, "//span[@class='pet_input__events events__submit __validation']")
    profileCardNumberClear = (By.XPATH, "//span[@class='pet_input__events events__clear']")
    profileCardPin = (By.CSS_SELECTOR, "input['formcontrolname=pin']")
    profileCardPinQuestion = (By.XPATH, "//span[@class='interface--icons input--question']")
    profileCardPinQuestionPopup = (By.XPATH, "//a[contains(text(),'Подробнее про Клуб')]")
    profileCardPinSubmit = (By.XPATH, "//span[@class='pet_input__events events__submit __validation']")
    profileCardDelete = (By.XPATH, "//p[@class='delete__card']")

    # Адреса доставок
    profileAddressArchway = (By.XPATH, "//span[@class='in__checked']")
    # profileAddressEdit = (By.XPATH, "")
    # profileAddressInput = (By.XPATH, "")
    profileAddressSave = (By.XPATH, "//div[@class='editable__save']")
    profileAddressCancel = (By.XPATH, "//div[@class='editable__cancel']")
    # profileAddressDelete = (By.XPATH, "")
    profileAddressDeleteYes = (By.XPATH, "//button[contains(text(),'Да, удалить')]")
    profileAddressDeleteNo = (By.XPATH, "//button[contains(text(),'Нет')]")

    # Мастера
    # profileMasterEdit = (By.CSS_SELECTOR, "")
    # profileMasterName = (By.CSS_SELECTOR, "")
    profileMasterPhone = (By.CSS_SELECTOR, "input['formcontrolname=phone']")
    profileMasterSave = (By.XPATH, "//div[@class='editable__save']")
    profileMasterCancel = (By.XPATH, "//div[@class='editable__cancel']")
    # profileMasterDelete = (By.CSS_SELECTOR, "")
    profileMasterDeleteYes = (By.XPATH, "//button[contains(text(),'Да, удалить')]")
    profileMasterDeleteNo = (By.XPATH, "//button[contains(text(),'Нет')]")

    # Контакты
    # profileContactEdit = (By.CSS_SELECTOR, "")
    # profileContactName = (By.CSS_SELECTOR, "")
    # profileContactEmail = (By.CSS_SELECTOR, "")
    profileContactPhone = (By.CSS_SELECTOR, "input['formcontrolname=phone']")
    profileContactSave = (By.XPATH, "//div[@class='editable__save']")
    profileContactCancel = (By.XPATH, "//div[@class='editable__cancel']")
    # profileContactDelete = (By.CSS_SELECTOR, "")
    profileContactDeleteYes = (By.XPATH, "//button[contains(text(),'Да, удалить')]")
    profileContactDeleteNo = (By.XPATH, "//button[contains(text(),'Нет')]")

    # Мои компании
    # profileCompanyDelete = (By.CSS_SELECTOR, "")
    profileCompanyDeleteYes = (By.XPATH, "//button[contains(text(),'Да, удалить')]")
    profileCompanyDeleteNo = (By.XPATH, "//button[contains(text(),'Нет')]")


class SearchOrdersHelperControls:

    # Поиск заказов
    ordersSearch = (By.CSS_SELECTOR, "input['formcontrolname=query']")
    ordersSearchDate = (By.XPATH, "//input[@class='__order__search_enter']")
    ordersSearchContractor = (By.XPATH, "//input[@class='__order__search_enter __js__dd--element']")


class CabinetOrdersHelperControls(SearchOrdersHelperControls):

    # Показать больше заказов
    ordersShowMore = (By.XPATH, "//p[@class='__upload']")
    ordersPopupContractors = (By.XPATH, "//div[@class='choose__data __js__dd__contractor']")
    ordersPopupSelectContractorCard = (By.CSS_SELECTOR, "div['data-value-inn=1231231231']")
    ordersPopupSelectContractorINN = (By.CSS_SELECTOR, "div['data-value-card=4269282']")
    ordersPopupPin = (By.XPATH, "//input[@class='card__pin __js__pin--input']")
    ordersPopupPinSubmit = (By.XPATH, "//button[@class='submit__pin __js__pin--submit']")
    ordersPopupHint = (By.XPATH, "//span[@class='hint__hover']")
    ordersPopupShowOrders = (By.XPATH, "//button[@class='__upload __js__upload--orders']")
    ordersPopupPreview = (By.XPATH, "//button[@class='__upload __js__upload--orders']")
    ordersPopupClose = (By.XPATH, "//div[@class='close__popup __js__popup--close']")

    # Фильтры заказов
    ordersFilterOnline = (By.XPATH, "//span[contains(text(),'Онлайн заказы')]")
    ordersFilterOffline = (By.XPATH, "//span[contains(text(),'Офлайн заказы')]")
    ordersFilterMobile = (By.XPATH, "//span[contains(text(),'Мобильные заказы')]")
    ordersFilterSelf = (By.XPATH, "//span[contains(text(),'Самовывоз')]")
    ordersFilterDelivery = (By.XPATH, "//span[contains(text(),'Доставка)]")
    ordersFilterInProgress = (By.XPATH, "//span[contains(text(),'В работе')]")
    ordersFilterFulfilled = (By.XPATH, "//span[contains(text(),'Выполненные')]")

    # Пагинация
    ordersPagination1 = (By.XPATH, "//li[contains(@class,'pagination_item')]//a[contains(text(),'1')]")
    ordersPagination2 = (By.XPATH, "//li[contains(@class,'pagination_item')]//a[contains(text(),'2')]")
    ordersPagination3 = (By.XPATH, "//li[contains(@class,'pagination_item')]//a[contains(text(),'3')]")
    ordersPaginationNext = (By.XPATH, "//i[@class='ic ic_arrow_next']")
    ordersPaginationFinish = (By.XPATH, "//i[@class='ic ic_arrow_finish']")


class CabinetProjectsHelperControls(SearchOrdersHelperControls):
    projectName = (By.XPATH, "//span[contains(text(),'test')]")