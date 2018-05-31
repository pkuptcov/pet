def test_city_change_msk(app):
    app.open_home_page()
    app.city.city_change_msk()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()


def test_city_change_nov(app):
    app.open_home_page()
    app.city.city_change_nov()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()


def test_city_change_vbg(app):
    app.open_home_page()
    app.city.city_change_vbg()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()


def test_city_change_gtn(app):
    app.open_home_page()
    app.city.city_change_gtn()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()


def test_city_change_lug(app):
    app.open_home_page()
    app.city.city_change_lug()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()


def test_city_change_kgs(app):
    app.open_home_page()
    app.city.city_change_kgs()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()


def test_city_change_pzv(app):
    app.open_home_page()
    app.city.city_change_pzv()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()


def test_city_change_tvr(app):
    app.open_home_page()
    app.city.city_change_nov()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()


def test_city_change_spb(app):
    app.open_home_page()
    app.city.city_change_spb()
    app.session.login(username="xigekuba@p33.org", password="111111")
    app.session.logout()