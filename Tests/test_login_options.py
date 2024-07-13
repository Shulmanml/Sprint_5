
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestData

class TestLoginOptions:

    def test_enter_from_enter_to_account_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        confirm_order_button = WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(TestLocators.CONFIRM_ORDER_BUTTON))
        assert confirm_order_button.is_displayed(), "Кнопка 'Оформить заказ' не появилась после успешной регистрации"

    def test_enter_from_my_account_button_success(self, driver):
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        confirm_order_button = WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(TestLocators.CONFIRM_ORDER_BUTTON))
        assert confirm_order_button.is_displayed(), "Кнопка 'Оформить заказ' не появилась после успешной регистрации"

    def test_enter_from_login_link_on_registration_form_success(self, driver):
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.LINK_TO_REGISTER).click()
        driver.find_element(*TestLocators.LOGIN_LINK_ON_REGISTRATION_FORM).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        confirm_order_button = WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(TestLocators.CONFIRM_ORDER_BUTTON))
        assert confirm_order_button.is_displayed(), "Кнопка 'Оформить заказ' не появилась после успешной регистрации"

    def test_enter_from_restore_password_link_success(self, driver):
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.RESTORE_PASSWORD_LINK).click()
        driver.find_element(*TestLocators.LOGIN_LINK_ON_REGISTRATION_FORM).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        confirm_order_button = WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(TestLocators.CONFIRM_ORDER_BUTTON))
        assert confirm_order_button.is_displayed(), "Кнопка 'Оформить заказ' не появилась после успешной регистрации"



