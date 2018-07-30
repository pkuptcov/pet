import random
import string


def test_register_gen(app):
    app.open_home_page()
    for i in range(10):
        app.register.register(firstname="test",
                              email=''.join(random.choices(string.ascii_lowercase + string.digits, k=20)) + "@kluatr.ru",
                              password="111111")
        app.session.logout()