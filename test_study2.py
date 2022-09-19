from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')

@pytest.fixture()
def configure_browser(open_browser):
    browser.config.window_width, browser.config.window_height == 1200, 800

def test_study(configure_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
