def test_login(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.search_product.search_product(product_name="гвоздь ондулин")
    app.catalog.quantity(qty="2")
    app.catalog.add_to_cart()
    app.cart_fiz.edit_card(card_number="111111")
    app.cart_fiz.init_order_self()

    app.thanks.order_link()
    app.session.logout()
