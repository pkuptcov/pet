# -*- coding: utf-8 -*-
# def test_auth(app):
#     app.open_home_page()
#     app.session.login(username="xigekuba@p33.org", password="111111")
#     app.session.logout()


# def test_fiz_delivery_auth(app):
#     app.open_home_page()
#     app.session.login(username="xigekuba@p33.org", password="111111")
#     app.regress.search()
#     app.regress.edit_quantity_product()
#     app.regress.go_to_cart()
#     app.regress.edit_card()
#     app.regress.init_order_creation_delivery()
#     app.regress.create_order_fiz_delivery()
#     app.regress.thanks()
#     app.session.logout()
#
#
def test_fiz_delivery_non_auth(app):
    app.open_home_page()
    app.regress.search()
    app.regress.edit_quantity_product()
    app.regress.go_to_cart()
    app.regress.edit_card()
    app.regress.init_order_creation_delivery()
    app.regress.create_order_fiz_delivery()
    app.regress.thanks()

#
# def test_fiz_self_auth(app):
#     app.open_home_page()
#     app.session.login(username="xigekuba@p33.org", password="111111")
#     app.regress.search()
#     app.regress.edit_quantity_product()
#     app.regress.go_to_cart()
#     app.regress.edit_card()
#     app.regress.init_order_creation_self()
#     app.regress.create_order_fiz_self()
#     app.regress.thanks()
#     app.session.logout()
#
#
# def test_fiz_self_non_auth(app):
#     app.open_home_page()
#     app.regress.search()
#     app.regress.edit_quantity_product()
#     app.regress.go_to_cart()
#     app.regress.edit_card()
#     app.regress.init_order_creation_self()
#     app.regress.create_order_fiz_self()
#     app.regress.thanks()
#
#
# def test_ur_delivery_auth(app):
#     app.open_home_page()
#     app.session.login(username="xigekuba@p33.org", password="111111")
#     app.regress.search()
#     app.regress.edit_quantity_product()
#     app.regress.go_to_cart()
#     app.regress.select_ur()
#     app.regress.init_order_creation_delivery()
#     app.regress.create_order_ur_delivery()
#     app.regress.thanks()
#     app.session.logout()
#
#
# def test_ur_delivery_non_auth(app):
#     app.open_home_page()
#     app.regress.search()
#     app.regress.edit_quantity_product()
#     app.regress.go_to_cart()
#     app.regress.select_ur()
#     app.regress.init_order_creation_delivery()
#     app.regress.create_order_ur_delivery()
#     app.regress.thanks()
#
#
# def test_ur_self_auth(app):
#     app.open_home_page()
#     app.session.login(username="xigekuba@p33.org", password="111111")
#     app.regress.search()
#     app.regress.edit_quantity_product()
#     app.regress.go_to_cart()
#     app.regress.select_ur()
#     app.regress.init_order_creation_self()
#     app.regress.create_order_ur_self()
#     app.regress.thanks()
#     app.session.logout()

#
# def test_ur_self_non_auth(app):
#     app.open_home_page()
#     app.regress.search()
#     app.regress.edit_quantity_product()
#     app.regress.go_to_cart()
#     app.regress.select_ur()
#     app.regress.init_order_creation_self()
#     app.regress.create_order_ur_self()
#     app.regress.thanks()