from selene import have, browser
from allure import step
from utils import allure_attach


def test_search():
    browser.open('/')

    with step('Type search'):
        browser.element('#searchInput').type('AppImage')

    with step('Verify content found'):
        results = browser.all('.suggestion-link')
        results.should(have.size_greater_than(0))
        results.first.should(have.text('AppImage'))
        allure_attach.add_screenshot(browser)
        allure_attach.add_video(browser)