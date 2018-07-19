import pytest
from ui_mobile.fixture.application import Application


@pytest.yield_fixture(scope="session", params=['firefox', 'chrome'])
def app(request):
    fixture = Application(browser=request.param)
    yield fixture
    fixture.destroy()