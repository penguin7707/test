import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find2(self, locator):
        return self.driver.find_elements(*locator)

    def click_1(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        CLICK_RETRY = 3
        while CLICK_RETRY > 0:
            try:
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except ElementClickInterceptedException:
                CLICK_RETRY = CLICK_RETRY - 1

    def log_in(self, user_email, user_password):
        self.click_1(basic_locators.LogIn_BUTTON_LOCATOR)
        email = self.find(basic_locators.LogIn_Email)
        email.send_keys(user_email)
        password = self.find(basic_locators.LogIn_Password)
        password.send_keys(user_password)
        self.click_1(basic_locators.LogIn_BUTTON2_LOCATOR)

    def log_out(self):
        self.find(basic_locators.LogOut)
        self.click_1(basic_locators.LogOut_BUTTON1_LOCATOR)
        self.click_1(basic_locators.LogOut_BUTTON2_LOCATOR)


    def change_info(self, user_name, user_phone, user_email):
        self.click_1(basic_locators.PROFILE_BUTTON)

        self.click_1(basic_locators.MORE_BUTTON)

        name_phone_email = self.find2(basic_locators.NAME_PHONE_EMAIL)
        name_phone_email[0].clear()
        name_phone_email[0].send_keys('user_name')

        name_phone_email[1].clear()
        name_phone_email[1].send_keys('user_phone')

        name_phone_email[2].send_keys('user_email')

        self.click_1(basic_locators.DELETE_BUTTON)

        self.click_1(basic_locators.SAVE_BUTTON)
