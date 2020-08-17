from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('https://location-software-np.groundtruth.com/')

time.sleep(10)
driver.maximize_window()
time.sleep(2)
# driver.execute_script('window.scrollBy(0,5000),""') # scroll by pixel
# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)') #scroll till the bottom of the page

# element=driver.find_element_by_xpath('//*[@id="lifenstylewidget"]') #scroll till the element is found
# # element=driver.find_element_by_link_text("About us ")
# driver.execute_script("arguments[0].scrollIntoView();", element)

# driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)
# driver.close()