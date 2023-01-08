import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


# MVP. В этом файле задаются настройки тестирования


@pytest.fixture()
def get_chrome_options():
    #  получение опций браузера
    options = chrome_options()
    options.add_argument('chrome')  # use headless if u don't need a browser UI
    options.add_argument('--start-maximized')  # окно открывается. как F11
    options.add_argument('--window-size=1280,720')  # разрешение окна
    return options


@pytest.fixture()
def get_webdriver(get_chrome_options):
    # получение драйвера браузера при заданных опциях
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')  # function отвечает за исполнение фикстуры каждый тест
# можно поставить аргумент session - раз в сессию
def setup(request, get_webdriver):
    # получение драйвера и отправление запроса на сайт
    driver = get_webdriver  # драйвер получается из метода
    url = 'https://www.wikipedia.org/' # задается url сайта, на котором будет проводиться тест.
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    # driver.delete_all_cookies()  # используется, потому что сайт ограничивает доступ к ресурсам из-за автоматизированного тестирования
    yield driver  # возврат driver, но не знаю почему используется yield
    driver.quit()  # закрытие всех окон, можно использовать driver.close(), но тогда закроется только одна вкладка теста
