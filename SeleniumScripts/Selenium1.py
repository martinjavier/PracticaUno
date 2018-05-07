
__author__ = "mjdp"

import datetime

from selenium import webdriver

driver = webdriver.Chrome("C:\\Webdrivers\\chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("http://newtours.demoaut.com")

driver.maximize.window()

driver.implicity_wait(20)

fecha = datetime.date

hora = datetime.time

captura = "Error"+fecha+hora

driver.get_screenshot_as_file(captura)


