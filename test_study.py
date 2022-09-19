from selene.support.shared import browser
from selene import be, have
def test_study():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('d66d6d6dsss').press_enter()
    browser.element('[id="topstuff"]').should(have.text('d66d6d6dsss'))

