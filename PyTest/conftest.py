import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="firefox",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: '--language=en' or '--language=ru'")
    parser.addoption('--browser_arg', action='store', default="disable-blink-features=AutomationControlled",
                     help='Example : --browser_arg=disable-blink-features=AutomationControlled')
    parser.addoption('--browser_headless', action='store', default="headless",
                     help='use space to disable --browser_headless=" "')


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    return language


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name", )
    language = request.config.getoption("language")
    browser_arg = request.config.getoption("browser_arg")
    browser_headless = request.config.getoption("browser_headless")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {'intl.accept_languages': language})
        chrome_options.add_argument(f'{browser_arg}')
        chrome_options.add_argument(f'--{browser_headless}')
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference(f'intl.accept_languages', f'{language}')
        firefox_options.add_argument(f'{browser_arg}')
        firefox_options.add_argument(f'--{browser_headless}')
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
