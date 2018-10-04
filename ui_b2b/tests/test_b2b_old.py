# -*- coding: utf-8 -*-


def test_ur_delivery_auth(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.smoke.select_city()
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.init_order_creation_delivery()
    app.smoke.create_order_ur_delivery()
    app.smoke.thanks()
    app.session.logout()


def test_ur_self_auth(app, settings):
    app.open_home_page()
    app.session.login(settings.LOGIN, settings.PASSWORD)
    app.smoke.select_city()
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.init_order_creation_self()
    app.smoke.create_order_ur_self()
    app.smoke.thanks()
    app.session.logout()