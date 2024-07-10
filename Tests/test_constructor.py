
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
        sauce_88 = driver.find_element(*TestLocators.SAUCE_88)
        assert sauce_88.text == "Соус с шипами Антарианского плоскоходца"

    def test_buns_section_click_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*TestLocators.SAUSE_SECTION).click()
        driver.find_element(*TestLocators.BUNS_SECTION).click()
        bun_1255 = driver.find_element(*TestLocators.BUN_1255)
        assert bun_1255.text == "Краторная булка N-200i"

    def test_toppings_section_success(self, driver):
        driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(TestData.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(TestData.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*TestLocators.TOPPINGS_SECTION).click()
        topping_4142 = driver.find_element(*TestLocators.TOPPING_4142)
        driver.execute_script("arguments[0].scrollIntoView();", topping_4142)
        assert topping_4142.text == "Сыр с астероидной плесенью"



