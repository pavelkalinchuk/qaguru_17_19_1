from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search(android_mobile_management):
    with step('Открыть поиск'):
        # Нажать на кнопку поиска
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with step('Ввести текст для поиска'):
        # Ввести текст "Appium" в поле поиска
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Проверить результаты поиска'):
        # Получить все элементы с результатами поиска
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))

        # Проверить, что список результатов не пуст
        results.should(have.size_greater_than(0))

        # Проверить, что первый результат содержит текст "Appium"
        results.first.should(have.text('Appium'))