
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestData

class TestConstructorAccessFromMyAccount:
    def test_enter_constructor_from_my_account_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        header_after_login = WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(TestLocators.HEADER_AFTER_LOGIN))
        assert header_after_login.is_displayed(), "Заголовок 'Соберите бургер' не появился после перехода из личного кабинета"

    def test_enter_constructor_from_my_account_logo_click_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.LOGO).click()
        header_after_login = WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(TestLocators.HEADER_AFTER_LOGIN))
        assert header_after_login.is_displayed(), "Заголовок 'Соберите бургер' не появился после перехода из личного кабинета"
