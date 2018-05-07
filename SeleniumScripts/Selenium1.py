__author__ = "mjdp"
__version__ = "1.0.0"
__email__ = "martin.delpercio@neoris.com"

import datetime
from libreriaUtiles import screenShot

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#DEFINICIONES
driver = webdriver.Chrome("C:\\Webdrivers\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://newtours.demoaut.com")
driver.maximize_window()
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 5)

screenShot(driver,"Login")

element = wait.until(EC.presence_of_element_located((By.NAME, "userName")))
driver.find_element_by_name("userName").send_keys("mercury")

element = wait.until(EC.presence_of_element_located((By.NAME, "password")))
driver.find_element_by_name("password").send_keys("mercury")

element = wait.until(EC.presence_of_element_located((By.NAME, "login")))
driver.find_element_by_name("login").click()

driver.implicitly_wait(3)

assert (EC.presence_of_element_located((By.NAME, "findFlights")))





#SALIDA
driver.implicitly_wait(1)
driver.quit()


