import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: '--language=en' or '--language=ru'")
    parser.addoption('--browser_arg', action='store', default="disable-blink-features=AutomationControlled",
                     help='Exaple : --browser_arg=disable-blink-features=AutomationControlled')


@pytest.fixture(scope="function")
def language(request) :
    language = request.config.getoption("language")
    return language
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name",)
    language = request.config.getoption("language")
    browser_arg=request.config.getoption("browser_arg")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {'intl.accept_languages': language})
        chrome_options.add_argument(f'--{browser_arg}')
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference(f'intl.accept_languages',f'{language}')
        firefox_options.add_argument(f'--{browser_arg}')
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
