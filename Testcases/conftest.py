from Env import config, browsers
import os

import pytest


@pytest.fixture(scope="class")
def driver():
    run_webdriver = browsers.mapping_browser[config.BROWSER]()
    yield run_webdriver
    run_webdriver.quit()


def pytest_logger_config(logger_config):
    logger_config.add_loggers(['test_barco'], stdout_level='debug')
    logger_config.set_log_option_default('test_barco')


def pytest_logger_logdirlink():
    return os.path.join(os.path.dirname(__file__), '../test.log')
