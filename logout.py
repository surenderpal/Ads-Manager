import login
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
# logout from Ads manager-----
def logout():
    driver.find_element_by_xpath("//button[@id='btn-userOptions-userOptionsMenuToggle']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//ul/li/a[text()='Sign Out']").click()
    time.sleep(4)
logout()
