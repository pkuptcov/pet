def test_delivery(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.header.select_spb()
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart.init_order_delivery()
    app.order_delivery.input_address(address="Россия, Санкт-Петербург, Благодатная улица, 6")
    app.order_delivery.select_day3()
    app.order_delivery.select_standart()
    app.order_delivery.select_interval()
    app.order_delivery.input_company_details(company_name='Тестовый контрагент', inn='1231231231', kpp='123123123')
    app.order_delivery.select_pay_noncash()
    app.order_delivery.input_email(email="info@kluatr.ru")
    app.order_delivery.input_phone(phone="(111) 111-11-11")
    app.order_delivery.input_username(username="Тест")
    app.order_delivery.input_comment(comment="тестовый заказ")
    app.order_delivery.submit_order()
    app.thanks.order_link()
    app.session.logout()


def test_self(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.header.select_spb()
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart.init_order_self()
    app.order_self.select_base()
    app.order_self.select_pay_noncash()
    app.order_self.input_company_details(company_name='Тестовый контрагент', inn='1231231231', kpp='123123123')
    app.order_self.input_email(email="info@kluatr.ru")
    app.order_self.input_phone(phone="(111) 111-11-11")
    app.order_self.input_username(username="Тест")
    app.order_self.input_comment(comment="тестовый заказ")
    app.order_self.submit_order()
    app.thanks.order_link()
    app.session.logout()