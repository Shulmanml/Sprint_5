from selenium.webdriver.common.by import By

class TestLocators:
    # кнопка личный кабинет
    MY_ACCOUNT_BUTTON = (By.XPATH, '//*[@class = "AppHeader_header__link__3D_hX"]/p[text() = "Личный Кабинет"]')

    # линк зарегистрироваться
    LINK_TO_REGISTER = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/register"]')

    # поле имя
    NAME_FIELD = (By.XPATH, '//label[text()="Имя"]/following-sibling::input[@name="name"]')

    # поле Email
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input[@name="name"]')

    #Поле пароль
    PASSWORD_FIELD = (By.XPATH, '//input[@name = "Пароль"]')

    # кнопка зарегистрироваться
    REGISTER_BUTTON = (By.XPATH, '//button[text() = "Зарегистрироваться"]')

    # кнопка войти
    LOGIN_BUTTON = (By.XPATH, '//button[text() = "Войти"]')

    # сообщение о некорректном пароле
    UNCORRECT_PASSWORD = (By.XPATH, '//p[text() = "Некорректный пароль"]')

    # кнопка Оформить заказ
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text() = "Оформить заказ"]')

    # кнопка войти в аккаунт
    ENTER_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[text() = "Войти в аккаунт"]')

    # линк войти в форме регистрации
    LOGIN_LINK_ON_REGISTRATION_FORM = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/login"]')

    # линк восстановить пароль
    RESTORE_PASSWORD_LINK = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/forgot-password"]')

    # кнопка сохранить в личном кабинете
    SAVE_BUTTON = (By.XPATH, '//div[@class = "Profile_buttonBox__1JlBI"]/button[text() = "Сохранить"]')

    # кнонка конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')

    # Заголовок страницы после входа
    HEADER_AFTER_LOGIN = (By.XPATH, '//h1[text() = "Соберите бургер"]')

    # лого сайта
    LOGO  = (By.XPATH, '//div[@class = "AppHeader_header__logo__2D0X2"]')

    # кнопка выход
    LOGOUT_BUTTON = (By.XPATH, '//button[text() = "Выход"]')

    # раздел соусы в меню
    SAUSE_SECTION = (By.XPATH, '//span[text() = "Соусы"]')

    # раздел булки в меню
    BUNS_SECTION = (By.XPATH, '//span[text() = "Булки"]')

    #раздел начинки в меню
    TOPPINGS_SECTION = (By.XPATH, '//span[text() = "Начинки"]')

    # соус цена которого 88 алмазов
    SAUCE_88 = (By.XPATH, '//p[text() = "Соус с шипами Антарианского плоскоходца"]')

    # детали соуса за 88 алмазов
    SAUCE_88_DETAILS = (By.XPATH, '//p[@class="text text_type_main-medium mb-8" and text() = "Соус с шипами Антарианского плоскоходца"]')

    # булка цена которой 1255 алмазов
    BUN_1255 = (By.XPATH, '//p[text() = "Краторная булка N-200i"]')

    # детали булки за 1255 алмазов
    BUN_1255_DETAILS = (By.XPATH, '//p[@class = "text text_type_main-medium mb-8" and text() = "Краторная булка N-200i"]')

    # начинка цена которой 4142 алмазов
    TOPPING_4142 = (By.XPATH, '//p[text() = "Сыр с астероидной плесенью"]')

    # детали начинки за 4142 алмазов
    TOPPING_4142_DETAILS = (By.XPATH, '//p[@class = "text text_type_main-medium mb-8" and text() = "Сыр с астероидной плесенью"]')









