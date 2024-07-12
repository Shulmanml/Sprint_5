from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestData

class TestRegistrationForm:
    def test_registration_success(self, driver):
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.LINK_TO_REGISTER).click()
        driver.find_element(*TestLocators.NAME_FIELD).send_keys(TestData.name)
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.registerlogin)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        login_button = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        assert login_button.is_displayed(), "Кнопка 'Войти' не появилась после успешной регистрации"

    def test_registration_failed(self, driver):
        driver.find_element(*TestLocators.MY_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.LINK_TO_REGISTER).click()
        driver.find_element(*TestLocators.NAME_FIELD).send_keys(TestData.name)
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.incorrect_password)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        uncorrect_password = driver.find_element(*TestLocators.UNCORRECT_PASSWORD)
        assert uncorrect_password.text == 'Некорректный пароль'

