import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def language(request) :
    language = request.config.getoption("language")
    return language
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name",)
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = Options()
        options.set_preference(f'intl.accept_languages',f'{language}')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
