import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestData

class TestConstructor:
    def test_sauce_section_click_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 1).until(
            expected_conditions.presence_of_element_located(TestLocators.HEADER_CONSTRUCTOR_PAGE))
        driver.find_element(*TestLocators.SAUSE_SECTION).click()
        assert WebDriverWait(driver, 1).until(
            expected_conditions.presence_of_element_located(TestLocators.SAUSE_SECTION_AFTER_CLICK))

    def test_buns_section_click_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 1).until(
            expected_conditions.presence_of_element_located(TestLocators.HEADER_CONSTRUCTOR_PAGE))
        driver.find_element(*TestLocators.SAUSE_SECTION).click()
        driver.find_element(*TestLocators.BUNS_SECTION).click()
        assert WebDriverWait(driver, 1).until(
            expected_conditions.presence_of_element_located(TestLocators.BUNS_SECTION_AFTER_CLICK))

    def test_toppings_section_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 1).until(
            expected_conditions.presence_of_element_located(TestLocators.HEADER_CONSTRUCTOR_PAGE))
        driver.find_element(*TestLocators.TOPPINGS_SECTION).click()
        assert WebDriverWait(driver, 1).until(
            expected_conditions.presence_of_element_located(TestLocators.TOPPINGS_SECTION_AFTER_CLICK))



