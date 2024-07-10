from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestData

class TestAccountAccessAfterLogin:
    def test_my_account_after_login_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        confirm_order_button = WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(TestLocators.SAVE_BUTTON))
        assert confirm_order_button.is_displayed(), "Кнопка 'Сохранить' не появилась после успешной регистрации"
