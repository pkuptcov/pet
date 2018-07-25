import pytest
from ui_desktop.fixture.application import Application


@pytest.yield_fixture(scope="session")
def chrome_app(settings):
    return Application('chrome', version=settings.CHROME_VERSION,  url=settings.URL,)


@pytest.yield_fixture(scope="session")
def firefox_app(settings):
    return Application('firefox', version=settings.FIREFOX_VERSION)


@pytest.yield_fixture(scope="session", params=['firefox_app', 'chrome_app'])
def complex_app(request):
    return request.getfixturevalue('request.param')


@pytest.yield_fixture(scope="session")
def app(request, settings):
    if settings.CHROME_VERSION:
        fixture = request.getfixturevalue('chrome_app')
    elif settings.FIREFOX_VERSION:
        fixture = request.getfixturevalue('firefox_app')
    else:
        fixture = request.getfixturevalue('chrome_app')

    yield fixture
    fixture.destroy()


@pytest.fixture(scope='session')
def settings(request):
    class Settings(object):
        CHROME_VERSION = None
        FIREFOX_VERSION = None
        URL = None
    a_settings = Settings()
    a_settings.CHROME_VERSION = request.config.option.chrome
    a_settings.FIREFOX_VERSION = request.config.option.firefox
    if not request.config.option.url:
        a_settings.URL = 'https://pet.beta.kluatr.ru/'
    else:
        a_settings.URL = 'http://petrovich.{}.pet.a'.format(request.config.option.url)
    return a_settings


def pytest_addoption(parser):
    parser.addoption('--chrome', default=None)
    parser.addoption('--firefox', default=None)
    parser.addoption('--url', default=None)
