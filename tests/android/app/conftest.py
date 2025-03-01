import os
import allure
import pytest
import allure_commons
from selene import browser, support
from appium import webdriver
from appium.options.android import UiAutomator2Options

from config import settings
from utils import allure_attach


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    # Настройка возможностей для BrowserStack
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': '9.0',  # Версия Android
        'deviceName': 'Google Pixel 3',  # Название устройства

        # Укажите URL или идентификатор приложения в BrowserStack
        'app': 'bs://sample.app',

        # Настройки BrowserStack
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Учетные данные для авторизации на BrowserStack
            'userName': settings.BROWSERSTACK_USER_NAME,
            'accessKey': settings.BROWSERSTACK_ACCESS_KEY,
        }
    })

    # Инициализация удаленного драйвера
    with allure.step('Инициализация сессии приложения'):
        browser.config.driver = webdriver.Remote(
            settings.BROWSERSTACK_URL,  # URL BrowserStack
            options=options
        )

    # Установка тайм-аута для Selene
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    # Настройка декоратора ожидания с поддержкой Allure
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    # Передача управления тесту
    yield

    # Прикрепление скриншота и XML к отчету Allure
    allure_attach.add_screenshot(browser)
    allure_attach.add_xml(browser)

    # Получение ID сессии для прикрепления видео
    session_id = browser.driver.session_id

    # Завершение сессии
    with allure.step('Завершение сессии приложения'):
        browser.quit()

    # Прикрепление видео из BrowserStack к отчету Allure
    allure_attach.add_bstack_video(session_id)