
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestData

class TestLogoutFromMyAccount:
    def test_logout_from_my_account_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 1).until(
            expected_conditions.presence_of_element_located(TestLocators.LOGOUT_BUTTON)).click()
        login_button = WebDriverWait(driver, 1).until(
            expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        assert login_button.is_displayed(), "Кнопка 'Войти' не появилась после выхода из личного кабинета"
