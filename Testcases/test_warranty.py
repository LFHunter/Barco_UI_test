from PageObject.warrantyinfo_page import WarrantyPage as wa_page
import pytest
import logging


class TestWarranty:
    default_error_msg = '[FAIL] {variable}, input_data:{input_data} ,\nactual: {actual}\nexpected: {expect}'
    logger = logging.getLogger("test_barco")
    wa_page = None

    @classmethod
    def setup_class(cls):
        cls.logger.info("Initial Test")

    @classmethod
    def teardown_class(cls):
        cls.logger.info("End Test")

    def setup_method(self, method):
        self.wa_page = TestWarranty.wa_page
        self.logger.info(f"----starting execution of tc: {method.__name__}----")

    def teardown_method(self, method):
        TestWarranty.wa_page = self.wa_page
        self.logger.info(f"----end execution of tc: {method.__name__}----")

    def gen_pageobject(self, driver, logger, back_basicpage=False):
        if not self.wa_page:
            self.logger.info(f"!!generate pageobject!!")
            self.wa_page = wa_page(driver, logger)
            self.wa_page.get_warranty_page()
            if back_basicpage:
                self.wa_page.get_warranty_page()

    def check(self, input_data, assert_variable, actual, expect):
        assert actual == expect, self.default_error_msg.format(input_data=input_data,
                                                               variable=assert_variable, actual=actual, expect=expect)

    @pytest.mark.parametrize('serial_number', ["1863552437"])
    def test_serial_number_positive_test(self, driver, serial_number):
        self.gen_pageobject(driver, self.logger)
        self.wa_page.search_serial_number(serial_number)
        result_dic = self.wa_page.get_search_successful_result()
        input_msg = f"serial_number:{serial_number}"

        self.check(input_msg, "description_title", result_dic["description_title"],
                   "Description")
        self.check(input_msg, "portnumber_title", result_dic["portnumber_title"],
                   "Part number")

        self.check(input_msg, "deliverydate_title", result_dic["deliverydate_title"],
                   "Delivery date")
        self.check(input_msg, "installationdate_title", result_dic["installationdate_title"],
                   "Installation date")
        self.check(input_msg, "warrantyenddate_title", result_dic["warrantyenddate_title"],
                   "Warranty end date")
        self.check(input_msg, "enddate_title", result_dic["enddate_title"],
                   "Service contract end date")

        self.check(input_msg, "description", result_dic["description"],
                   "CLICKSHARE CX-50 SET NA")
        self.check(input_msg, "portnumber", result_dic["portnumber"],
                   "R9861522NA")
        self.check(input_msg, "deliverydate", result_dic["deliverydate"],
                   "05/07/2020 00:00:00")
        self.check(input_msg, "installationdate", result_dic["installationdate"],
                   "09/28/2020 09:16:22")
        self.check(input_msg, "warrantyenddate", result_dic["warrantyenddate"],
                   "09/27/2021 09:16:22")
        self.check(input_msg, "enddate", result_dic["enddate"],
                   "01/01/0001 00:00:00")

    @pytest.mark.parametrize('serial_number', ["9863552437", "aA863552437"])
    def test_serial_number_negative_test(self, driver, serial_number):
        self.gen_pageobject(driver, self.logger)
        self.wa_page.search_serial_number(serial_number)
        result_dic = self.wa_page.get_search_fail_result()
        self.check(f"serial_number:{serial_number}", "result_title", result_dic["result_title"],
                   f"Warranty results for {serial_number}")
        self.check(f"serial_number:{serial_number}", "result_detail_msg", result_dic["result_detail_msg"],
                   "We couldn't find a product with this serial number. Please double-check"
                   " the serial number and try again.")

    @pytest.mark.parametrize('serial_number', ["12345"])
    def test_serial_number_less_than_5_words_boundary_test(self, driver, serial_number):
        self.gen_pageobject(driver, self.logger)
        self.wa_page.search_serial_number(serial_number)
        hint = self.wa_page.get_too_short_hint()
        self.check(f"serial_number:{serial_number}", "too_short_hint", actual=hint,
                   expect="Minimum 6 characters required")

    @pytest.mark.parametrize('serial_number', ["123456", "1234567"])
    def test_serial_number_for_equal_or_more_than_6_words_boundary_test(self, driver, serial_number):
        self.gen_pageobject(driver, self.logger)
        self.wa_page.search_serial_number(serial_number)
        result_dic = self.wa_page.get_search_fail_result()
        self.check(f"serial_number:{serial_number}", "result_title", result_dic["result_title"],
                   f"Warranty results for {serial_number}")
        self.check(f"serial_number:{serial_number}", "result_detail_msg", result_dic["result_detail_msg"],
                   "We couldn't find a product with this serial number. Please double-check"
                   " the serial number and try again.")

    @pytest.mark.parametrize('serial_number', ["!12345", "!@222#$%"])
    def test_serial_number_different_special_characters_test(self, driver, serial_number):
        self.gen_pageobject(driver, self.logger)
        self.wa_page.search_serial_number(serial_number)
        hint = self.wa_page.get_error_format_serialnumber_hint()
        self.check(f"serial_number:{serial_number}", "error_format_hint", actual=hint,
                   expect="Please enter a valid serial number")
