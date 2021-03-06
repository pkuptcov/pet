import pytest
from ui_mobile.application import Application


@pytest.yield_fixture(scope="session")
def chrome_app(settings):
    return Application('chrome', version=settings.CHROME_VERSION, url=settings.URL)


@pytest.yield_fixture(scope="session")
def app(request, settings):
    if settings.CHROME_VERSION:
        fixture = request.getfixturevalue('chrome_app')
    else:
        fixture = request.getfixturevalue('chrome_app')

    yield fixture
    fixture.destroy()


@pytest.fixture(scope='session')
def settings(request):
    class Settings(object):
        CHROME_VERSION = None
        URL = None
        LOGIN = None
        PASSWORD = None

    a_settings = Settings()
    a_settings.CHROME_VERSION = request.config.option.chrome
    a_settings.LOGIN = request.config.option.login
    a_settings.PASSWORD = request.config.option.password

    if not request.config.option.url:
        a_settings.URL = 'https://pet.beta.kluatr.ru/'
    else:
        a_settings.URL = 'http://petrovich.{}.pet.a'.format(request.config.option.url)
    return a_settings


def pytest_addoption(parser):
    parser.addoption('--chrome', default=None)
    parser.addoption('--url', default=None)
    parser.addoption('--login', default=None)
    parser.addoption('--password', default=None)