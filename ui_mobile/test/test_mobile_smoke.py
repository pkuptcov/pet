# -*- coding: utf-8 -*-


def test_fiz_delivery_auth(app):
    app.open_home_page()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.edit_card()
    app.smoke.init_order_creation_delivery()
    app.smoke.create_order_fiz_delivery()
    app.smoke.thanks()
    app.session.logout()


def test_fiz_delivery_non_auth(app):
    app.open_home_page()
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.edit_card()
    app.smoke.init_order_creation_delivery()
    app.smoke.create_order_fiz_delivery()
    app.smoke.thanks()


def test_fiz_self_auth(app):
    app.open_home_page()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.edit_card()
    app.smoke.init_order_creation_self()
    app.smoke.create_order_fiz_self()
    app.smoke.thanks()
    app.session.logout()


def test_fiz_self_non_auth(app):
    app.open_home_page()
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.edit_card()
    app.smoke.init_order_creation_self()
    app.smoke.create_order_fiz_self()
    app.smoke.thanks()


def test_ur_delivery_auth(app):
    app.open_home_page()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.select_ur()
    app.smoke.init_order_creation_delivery()
    app.smoke.create_order_ur_delivery()
    app.smoke.thanks()
    app.session.logout()


def test_ur_delivery_non_auth(app):
    app.open_home_page()
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.select_ur()
    app.smoke.init_order_creation_delivery()
    app.smoke.create_order_ur_delivery()
    app.smoke.thanks()


def test_ur_self_auth(app):
    app.open_home_page()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.select_ur()
    app.smoke.init_order_creation_self()
    app.smoke.create_order_ur_self()
    app.smoke.thanks()
    app.session.logout()


def test_ur_self_non_auth(app):
    app.open_home_page()
    app.smoke.search()
    app.smoke.edit_quantity_product()
    app.smoke.go_to_cart()
    app.smoke.select_ur()
    app.smoke.init_order_creation_self()
    app.smoke.create_order_ur_self()
    app.smoke.thanks()