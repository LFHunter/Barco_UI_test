from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def chromebrowser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument("--disable-gpu")
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    chrome_driver.maximize_window()
    return chrome_driver


def safaribrowser():
    return None


mapping_browser = {"CHROME": chromebrowser,
                   "SAFARI": safaribrowser}

