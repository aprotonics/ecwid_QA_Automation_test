import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# For Chromium
from webdriver_manager.utils import ChromeType


@pytest.fixture(scope='function')
def driver(request):
    browser_name = 'chrome'
    driver = None
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--remote-debugging-port=9222")

        # For Chrome
        # service=Service(ChromeDriverManager().install())

        # For Chromium
        service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        driver = webdriver.Chrome(service=service, options=options)

    if browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        options.add_argument('--ignore-certificate-errors')

        service=Service(GeckoDriverManager().install())

        driver = webdriver.Firefox(service=service, options=options)

        driver.maximize_window()
    
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
