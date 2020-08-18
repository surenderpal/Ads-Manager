from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


driver=webdriver.Chrome()
driver.get('https://location-software-np.groundtruth.com/')

time.sleep(10)
# driver.execute_script('window.scrollBy(0,5000),""') # scroll by pixel
# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)') #scroll till the bottom of the page
# element=driver.find_element_by_xpath('//*[@id="lifenstylewidget"]') #scroll till the element is found
# # element=driver.find_element_by_link_text("About us ")
# driver.execute_script("arguments[0].scrollIntoView();", element)

# driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)
# driver.close()
def login(Username,Password):
    driver.find_element_by_name('username').send_keys(Username)
    driver.find_element_by_name('password').send_keys(Password)
    driver.find_element_by_id('submit').click()

login('surender.pal@groundtruth.com','Surenderpal@1991')

time.sleep(5)
print('Login successfully in location software')
driver.find_element_by_xpath("//div[@class='hamburger-icon']").click() #hamburger menu

i=driver.find_element_by_xpath("//a[@class='info-circle-button']")
brands=driver.find_element_by_xpath("//span[contains(text(),'Brands')]") 
LG=driver.find_element_by_xpath("//span[contains(text(),'Location Groups')]")



actions=ActionChains(driver)
actions.move_to_element(brands).move_to_element(LG).click().perform()
