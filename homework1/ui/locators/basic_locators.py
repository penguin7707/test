from selenium.webdriver.common.by import By


LogIn_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "responseHead-module-button")]')
LogIn_Email = (By.NAME, 'email')
LogIn_Password = (By.NAME, 'password')
LogIn_BUTTON2_LOCATOR = (By.XPATH, '//*[contains(@class, "authForm-module-button")]')

LogOut_BUTTON1_LOCATOR = (By.XPATH, '//*[contains(@class, "right-module-rightButton")]')
LogOut_BUTTON2_LOCATOR = (By.XPATH, '//ul[contains(@class, "rightMenu-module-rightMenu")]/li[2]')
LogOut = (By.XPATH, '//*[contains(@class, "instruction-module-title")]')

PROFILE_BUTTON = (By.XPATH, '//*[contains(@class, "center-module-buttonsWrap")]/li[6]/a')
NAME_PHONE_EMAIL = (By.CLASS_NAME, 'input__inp.js-form-element')
MORE_BUTTON = (By.XPATH, '//*[contains(@class, "clickable-button__spinner")]')
DELETE_BUTTON = (By.XPATH, '//*[contains(@class, "clickable-button_email_remove")]')
SAVE_BUTTON = (By.CLASS_NAME, 'button__text')

CHANGE_PAGE1 = (By.XPATH, '//*[contains(@class, "center-module-buttonsWrap")]/li[6]/a')
CHANGE_PAGE2 = (By.XPATH, '//*[contains(@class, "center-module-buttonsWrap")]/li[3]/a')
ELEM = (By.TAG_NAME, 'input')