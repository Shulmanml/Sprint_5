
from locators import TestLocators
from data import TestData

class TestConstructor:
    def test_sauce_section_click_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*TestLocators.SAUSE_SECTION).click()
        driver.find_element(*TestLocators.SAUCE_88).click()
        sauce_88_details = driver.find_element(*TestLocators.SAUCE_88_DETAILS)
        assert sauce_88_details.text == "Соус с шипами Антарианского плоскоходца"

    def test_buns_section_click_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*TestLocators.BUN_1255).click()
        bun_1255_details = driver.find_element(*TestLocators.BUN_1255_DETAILS)
        assert bun_1255_details.text == "Краторная булка N-200i"

    def test_toppings_section_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*TestLocators.TOPPINGS_SECTION).click()
        topping_4142 = driver.find_element(*TestLocators.TOPPING_4142)
        driver.execute_script("arguments[0].scrollIntoView();", topping_4142)
        topping_4142.click()
        topping_4142_details = (driver.find_element(*TestLocators.TOPPING_4142_DETAILS))
        assert topping_4142_details.text == "Сыр с астероидной плесенью"



