import random
import string


def test_register_gen(app):
    app.open_home_page()
    n = 10
    for i in range(n):
        app.register.register(firstname="test",
                              lastname="test",
                              email=''.join(random.choices(string.ascii_lowercase + string.digits, k=20)) + "@kluatr.ru",
                              password="111111",
                              kkd="1111111")
        app.session.logout()