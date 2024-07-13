import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope = 'function')
def driver():
    options = Options()
    options.add_argument("--window-size=1200,800")
    driver = webdriver.Chrome(options=options)
    url = 'https://stellarburgers.nomoreparties.site/'
    driver.get(url)
    yield driver
    driver.quit()