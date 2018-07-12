# -*- coding: utf-8 -*-
# def test_auth_logout(app):
#     app.open_home_page()
#     app.session.login(login="pavel.kuptcov@gmail.com", password="111111")
#     app.session.logout()


def test_ur_delivery_auth(app):
    app.open_home_page()
    app.session.login(login="pavel.kuptcov@gmail.com", password="111111")
    app.regress.select_city()
    app.regress.search()
    app.regress.edit_quantity_product()
    app.regress.go_to_cart()
    app.regress.init_order_creation_delivery()
    app.regress.create_order_ur_delivery()
    app.regress.thanks()
    app.session.logout()


def test_ur_self_auth(app):
    app.open_home_page()
    app.session.login(login="pavel.kuptcov@gmail.com", password="111111")
    app.regress.select_city()
    app.regress.search()
    app.regress.edit_quantity_product()
    app.regress.go_to_cart()
    app.regress.init_order_creation_self()
    app.regress.create_order_ur_self()
    app.regress.thanks()
    app.session.logout()