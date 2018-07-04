import pytest
from ui_desktop.fixture.application import Application


@pytest.yield_fixture(scope="session")
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()