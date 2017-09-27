# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def fiz_delivery_auth(app):
    app.open_home_page()
    app.login(username="xigekuba@p33.org", password="111111")
    app.search()
    app.edit_quantity_product()
    app.go_to_cart()
    app.edit_card()
    app.init_order_creation()
    app.create_order()
    app.thanks()
    app.logout()