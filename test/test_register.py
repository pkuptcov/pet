from random import choice
from string import ascii_letters
import time


def test_register_gen(app):
    app.open_home_page()
    for i in range(10):
        app.register.register(firstname="test",email=(''.join(choice(ascii_letters) for i in range(14))) + "@test.test", password="111111")
        #time.sleep(1)
        app.session.logout()