def test_fiz_delivery_auth(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_fiz.select_fiz()
    app.cart_fiz.edit_card(card_number="111111")
    app.cart_fiz.init_order_delivery()
    app.order_delivery_fiz.input_address(address="Россия, Санкт-Петербург, Благодатная улица, 6")
    app.order_delivery_fiz.select_day3()
    app.order_delivery_fiz.select_standart()
    app.order_delivery_fiz.select_interval()
    app.order_delivery_fiz.select_pay_online()
    app.order_delivery_fiz.input_email(email="info@kluatr.ru")
    app.order_delivery_fiz.input_phone(phone="(111) 111-11-11")
    app.order_delivery_fiz.input_username(username="Тест")
    app.order_delivery_fiz.input_comment(comment="тестовый заказ")
    app.order_delivery_fiz.submit_order()
    app.thanks.order_link()
    app.session.logout()


def test_fiz_delivery_non_auth(app):
    app.open_home_page()
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_fiz.select_fiz()
    app.cart_fiz.edit_card(card_number="111111")
    app.cart_fiz.init_order_delivery()
    app.order_delivery_fiz.input_address(address="Россия, Санкт-Петербург, Благодатная улица, 6")
    app.order_delivery_fiz.select_day3()
    app.order_delivery_fiz.select_standart()
    app.order_delivery_fiz.select_interval()
    app.order_delivery_fiz.select_pay_online()
    app.order_delivery_fiz.input_email(email="info@kluatr.ru")
    app.order_delivery_fiz.input_phone(phone="(111) 111-11-11")
    app.order_delivery_fiz.input_username(username="Тест")
    app.order_delivery_fiz.input_comment(comment="тестовый заказ")
    app.order_delivery_fiz.submit_order()
    app.thanks.order_link()


def test_fiz_self_auth(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_fiz.select_fiz()
    app.cart_fiz.edit_card(card_number="111111")
    app.cart_fiz.init_order_self()
    app.order_self_fiz.select_base()
    app.order_self_fiz.select_pay_online()
    app.order_self_fiz.input_email(email="info@kluatr.ru")
    app.order_self_fiz.input_phone(phone="(111) 111-11-11")
    app.order_self_fiz.input_username(username="Тест")
    app.order_self_fiz.input_comment(comment="тестовый заказ")
    app.order_self_fiz.submit_order()
    app.thanks.order_link()
    app.session.logout()


def test_fiz_self_non_auth(app):
    app.open_home_page()
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_fiz.select_fiz()
    app.cart_fiz.edit_card(card_number="111111")
    app.cart_fiz.init_order_self()
    app.order_self_fiz.select_base()
    app.order_self_fiz.select_pay_online()
    app.order_self_fiz.input_email(email="info@kluatr.ru")
    app.order_self_fiz.input_phone(phone="(111) 111-11-11")
    app.order_self_fiz.input_username(username="Тест")
    app.order_self_fiz.input_comment(comment="тестовый заказ")
    app.order_self_fiz.submit_order()
    app.thanks.order_link()


def test_ur_delivery_auth(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_ur.select_ur()
    app.cart_ur.init_order_delivery()
    app.order_delivery_ur.input_address(address="Россия, Санкт-Петербург, Благодатная улица, 6")
    app.order_delivery_ur.select_day3()
    app.order_delivery_ur.select_standart()
    app.order_delivery_ur.select_interval()
    app.order_delivery_ur.input_company_details(company_name='Тестовый контрагент', inn='1231231231', kpp='123123123')
    app.order_delivery_ur.select_pay_noncash()
    app.order_delivery_ur.input_email(email="info@kluatr.ru")
    app.order_delivery_ur.input_phone(phone="(111) 111-11-11")
    app.order_delivery_ur.input_username(username="Тест")
    app.order_delivery_ur.input_comment(comment="тестовый заказ")
    app.order_delivery_ur.submit_order()
    app.thanks.order_link()
    app.session.logout()


def test_ur_delivery_non_auth(app):
    app.open_home_page()
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_ur.select_ur()
    app.cart_ur.init_order_delivery()
    app.order_delivery_ur.input_address(address="Россия, Санкт-Петербург, Благодатная улица, 6")
    app.order_delivery_ur.select_day3()
    app.order_delivery_ur.select_standart()
    app.order_delivery_ur.select_interval()
    app.order_delivery_ur.input_company_details(company_name='Тестовый контрагент', inn='1231231231', kpp='123123123')
    app.order_delivery_ur.select_pay_noncash()
    app.order_delivery_ur.input_email(email="info@kluatr.ru")
    app.order_delivery_ur.input_phone(phone="(111) 111-11-11")
    app.order_delivery_ur.input_username(username="Тест")
    app.order_delivery_ur.input_comment(comment="тестовый заказ")
    app.order_delivery_ur.submit_order()
    app.thanks.order_link()


def test_ur_self_auth(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_ur.select_ur()
    app.cart_ur.init_order_self()
    app.order_self_ur.select_base()
    app.order_self_ur.select_pay_noncash()
    app.order_self_ur.input_company_details(company_name='Тестовый контрагент', inn='1231231231', kpp='123123123')
    app.order_self_ur.input_email(email="info@kluatr.ru")
    app.order_self_ur.input_phone(phone="(111) 111-11-11")
    app.order_self_ur.input_username(username="Тест")
    app.order_self_ur.input_comment(comment="тестовый заказ")
    app.order_self_ur.submit_order()
    app.thanks.order_link()
    app.session.logout()


def test_ur_self_non_auth(app):
    app.open_home_page()
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_ur.select_ur()
    app.cart_ur.init_order_self()
    app.order_self_ur.select_base()
    app.order_self_ur.select_pay_noncash()
    app.order_self_ur.input_company_details(company_name='Тестовый контрагент', inn='1231231231', kpp='123123123')
    app.order_self_ur.input_email(email="info@kluatr.ru")
    app.order_self_ur.input_phone(phone="(111) 111-11-11")
    app.order_self_ur.input_username(username="Тест")
    app.order_self_ur.input_comment(comment="тестовый заказ")
    app.order_self_ur.submit_order()
    app.thanks.order_link()