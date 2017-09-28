# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_fiz_delivery_auth(app):
    app.open_home_page()
    app.login(username="xigekuba@p33.org", password="111111")
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.edit_card()
    app.init_order_creation_delivery()
    app.create_order_fiz_delivery()
    app.thanks()
    app.logout()


def test_fiz_delivery_non_auth(app):
    app.open_home_page()
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.edit_card()
    app.init_order_creation_delivery()
    app.create_order_fiz_delivery()
    app.thanks()


def test_fiz_self_auth(app):
    app.open_home_page()
    app.login(username="xigekuba@p33.org", password="111111")
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.edit_card()
    app.init_order_creation_self()
    app.create_order_fiz_self()
    app.thanks()
    app.logout()


def test_fiz_self_non_auth(app):
    app.open_home_page()
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.edit_card()
    app.init_order_creation_self()
    app.create_order_fiz_self()
    app.thanks()


def test_ur_delivery_auth(app):
    app.open_home_page()
    app.login(username="xigekuba@p33.org", password="111111")
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.select_ur()
    app.init_order_creation_delivery()
    app.create_order_ur_delivery()
    app.thanks()
    app.logout()


def test_ur_delivery_non_auth(app):
    app.open_home_page()
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.select_ur()
    app.init_order_creation_delivery()
    app.create_order_ur_delivery()
    app.thanks()


def test_ur_self_auth(app):
    app.open_home_page()
    app.login(username="xigekuba@p33.org", password="111111")
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.select_ur()
    app.init_order_creation_self()
    app.create_order_ur_self()
    app.thanks()
    app.logout()


def test_ur_self_non_auth(app):
    app.open_home_page()
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.select_ur()
    app.init_order_creation_self()
    app.create_order_ur_self()
    app.thanks()