from Locators import warrantyinfo_locator as wa_locator
from BaseLib.base_page import BasePage
from Locators import urls


class WarrantyPage(BasePage):

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger_msg = "=====[{msg}]=====" + f"{self.driver}"
        self.driver.set_page_load_timeout(45)

    def get_warranty_page(self):
        self.logger.debug(self.logger_msg.format(msg=f"get_warranty_page:{urls.warranty_url}"))
        try:
            self.driver.get(urls.warranty_url)
            self.logger.debug(f"Successfully get {urls.warranty_url}")
        except Exception as exp:
            self.logger.debug(f"Exception:{exp}")
            self.logger.debug(f"get {urls.warranty_url} again")
            self.driver.get(urls.warranty_url)
        super().wait_ele_visible(wa_locator.H1_warranty_intro, 5)
        super().wait_ele_clickable(wa_locator.INPUT_serial_number, 5)

    def input_serial_number(self, serial_number):
        self.logger.debug(self.logger_msg.format(msg=f"input_serial_number:{serial_number}"))
        super().send_keys(wa_locator.INPUT_serial_number, serial_number)

    def click_get_info(self):
        self.logger.debug(self.logger_msg.format(msg="click_get_info"))
        super().click(wa_locator.BUTTON_get_info)

    def search_serial_number(self, serial_number):
        self.input_serial_number(serial_number)
        self.click_get_info()

    def accept_cookies_prompt(self):
        self.logger.debug(self.logger_msg.format(msg="accept_cookies_prompt"))
        super().wait_ele_visible(wa_locator.div_prompt, 10)
        super().click(wa_locator.button_prompt_accept, 10)

    def get_clickshare_title(self):
        self.logger.debug(self.logger_msg.format(msg="get_clickshare_title"))
        return super().get_text(wa_locator.H1_warranty_intro)

    def get_too_short_hint(self):
        self.logger.debug(self.logger_msg.format(msg="get_too_short_hint"))
        hint = super().get_text(wa_locator.SPAN_showIsTooShort)
        return hint

    def get_error_format_serialnumber_hint(self):
        self.logger.debug(self.logger_msg.format(msg="get_error_format_serialnumber_hint"))
        hint = super().get_text(wa_locator.SPAN_showIsWrongFormat)
        return hint

    def get_search_fail_result(self):
        self.logger.debug(self.logger_msg.format(msg="get_search_fail_result"))
        result_title = super().get_text(
            wa_locator.H2_fail_find_result_title)
        result_detail_msg = super().get_text(wa_locator.P_fail_find_detail_msg)
        return locals()

    def get_search_successful_result(self):
        self.logger.debug(self.logger_msg.format(msg="get_search_successful_result"))
        description_title = super().get_text(wa_locator.dt_successfully_find_product_result_description_title)
        portnumber_title = super().get_text(wa_locator.dt_successfully_find_product_result_portnumber_title)
        deliverydate_title = super().get_text(wa_locator.dt_successfully_find_product_result_deliverydate_title)
        installationdate_title = super().get_text(
            wa_locator.dt_successfully_find_product_result_installationdate_title)
        warrantyenddate_title = super().get_text(
            wa_locator.dt_successfully_find_product_result_warrantyenddate_title)
        enddate_title = super().get_text(
            wa_locator.dt_successfully_find_product_result_enddate_title)

        description = super().get_text(wa_locator.dl_successfully_find_product_result_description)
        portnumber = super().get_text(wa_locator.dl_successfully_find_product_result_portnumber)
        deliverydate = super().get_text(wa_locator.dl_successfully_find_product_result_deliverydate)
        installationdate = super().get_text(
            wa_locator.dl_successfully_find_product_result_installationdate)
        warrantyenddate = super().get_text(
            wa_locator.dl_successfully_find_product_result_warrantyenddate)
        enddate = super().get_text(
            wa_locator.dl_successfully_find_product_result_enddate)

        return locals()
