from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


driver=webdriver.Chrome()
# driver.get('https://location-software-np.groundtruth.com/')
# time.sleep(2)
# # driver.execute_script('window.scrollBy(0,5000),""') # scroll by pixel
# # driver.execute_script('window.scrollBy(0,document.body.scrollHeight)') #scroll till the bottom of the page
# # element=driver.find_element_by_xpath('//*[@id="lifenstylewidget"]') #scroll till the element is found
# # # element=driver.find_element_by_link_text("About us ")
# # driver.execute_script("arguments[0].scrollIntoView();", element)

# # driver.execute_script("arguments[0].scrollIntoView();", element)
# # time.sleep(2)
# # driver.close()
# def login(Username,Password):
#     driver.find_element_by_name('username').send_keys(Username)
#     driver.find_element_by_name('password').send_keys(Password)
#     driver.find_element_by_id('submit').click()

# # login('surender.pal@groundtruth.com','Surenderpal@1991')
# time.sleep(2)
# print('Login successfully in location software')
# driver.find_element_by_xpath("//div[@class='hamburger-icon']").click() #hamburger menu

# i=driver.find_element_by_xpath("//a[@class='info-circle-button']")
# brands=driver.find_element_by_xpath("//span[contains(text(),'Brands')]") 
# LG=driver.find_element_by_xpath("//span[contains(text(),'Location Groups')]")
# actions=ActionChains(driver)
# actions.move_to_element(brands).move_to_element(LG).click().perform()
# am=driver.find_element_by_xpath("//button[contains(text(),'Audience Manager')]")
# lm=driver.find_element_by_xpath("//button[contains(text(),'Location Manager ')]")
# time.sleep(2)
# info=driver.find_element_by_xpath("//div[@class='dropdown-info-container']/div[@class='info-container']")
# # info.click()
# actions.move_to_element(am).move_to_element(lm).click().perform() #.move_to_element(info)
# print('clicked on info')

# #----hover pratice-----
# driver.get('https://yomovies.link/')
# driver.maximize_window()
# genre=driver.find_element_by_xpath("//li/a[(contains(text(), 'Genre'))]")
# action=driver.find_element_by_xpath("//li/a[(contains(text(), 'Action'))]")
# biography=driver.find_element_by_xpath("//li/a[(contains(text(), 'Biography'))]")
# music=driver.find_element_by_xpath("//li/a[(contains(text(), 'Music'))]")
# fantasy=driver.find_element_by_xpath("//li/a[(contains(text(), 'Fantasy'))]")
# Fiction=driver.find_element_by_xpath("//li/a[(contains(text(), 'Science Fiction'))]")
# Adventure=driver.find_element_by_xpath("//li/a[(contains(text(), 'Adventure'))]")
# Comedy=driver.find_element_by_xpath("//li/a[(contains(text(), 'Comedy'))]")
# War=driver.find_element_by_xpath("//li/a[(contains(text(), 'War'))]")
# actions=ActionChains(driver)
# actions.move_to_element(genre).move_to_element(action).move_to_element(biography).move_to_element(music).move_to_element(fantasy).move_to_element(Fiction).move_to_element(Adventure).move_to_element(Comedy).move_to_element(War).click().perform()
# print('learnt hover')
