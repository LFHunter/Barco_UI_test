from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert


class BasePage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def wait_ele_visible(self, locator, timeout=10):
        self.logger.debug(f"wait_ele_visible: {locator}, timeout:{timeout}")
        ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return ele

    def wait_ele_clickable(self, locator, timeout=10):
        self.logger.debug(f"wait_ele_clickable: {locator}, timeout:{timeout}")
        ele = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return ele

    def click(self, locator, timeout=10):
        self.logger.debug(f"click element: {locator}, timeout:{timeout}")
        ele = self.wait_ele_clickable(locator, timeout=timeout)
        ele.click()

    def send_keys(self, locator, msg, timeout=10):
        print(f"send_keys: {locator}, timeout:{timeout}")
        self.logger.debug(f"send_keys: {locator}, timeout:{timeout}")
        ele = self.wait_ele_clickable(locator, timeout=timeout)
        ele.clear()
        ele.send_keys(msg)
        ele_value = self.get_value(locator, timeout=timeout)
        if str(msg) != str(ele_value):
            self.logger.debug(f"input: {msg}, element value:{ele_value}")
            raise f"[ERROR]\ninput: {msg} not equal to\nelement value:{ele_value}"

    def get_text(self, locator, timeout=10):
        self.logger.debug(f"get_text: {locator}, timeout:{timeout}")
        ele = self.wait_ele_visible(locator, timeout=timeout)
        return ele.text

    def get_value(self, locator, timeout=10):
        self.logger.debug(f"get_value: {locator}, timeout:{timeout}")
        ele = self.wait_ele_visible(locator, timeout=timeout)
        return ele.get_attribute("value")

    def get_alert(self, timeout=10):
        self.logger.debug(f"get_alert, timeout:{timeout}")
        alert = Alert(self.driver)
        return alert
