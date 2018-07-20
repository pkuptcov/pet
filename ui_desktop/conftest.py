import pytest
from ui_desktop.fixture.application import Application


@pytest.yield_fixture(scope="session", params=['firefox', 'chrome'])
def app(request, settings):
    fixture = Application(request.param, chrome_version=settings.CHROME_VERSION, firefox_version=settings.FIREFOX_VERSION)
    yield fixture
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption('--chrome', default=66)
    parser.addoption('--firefox', default=60)


@pytest.fixture(scope='session')
def settings(request):
    class Settings(object):
       CHROME_VERSION = None
       FIREFOX_VERSION = None
    a_settings = Settings()
    a_settings.CHROME_VERSION = str(request.config.option.chrome)
    a_settings.FIREFOX_VERSION = str(request.config.option.firefox)
    return a_settings