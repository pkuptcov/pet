from random import choice
from string import ascii_letters


def test_register_gen(app):
    app.open_home_page_b2b()
    for i in range(1):
        app.register.register(lastname="Тестов", firstname="Тест", company="Тестовая", inn="1231231231",
                              email=('test'.join(choice(ascii_letters) for i in range(10))) + "@kluatr.ru",
                              phone="111111111")