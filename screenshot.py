from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://www.amazon.in/')
time.sleep(2)
driver.save_screenshot('/Users/surenderpal/Projects/Ads-Manager/Screenshots/amazon.PNG')
driver.get_screenshot_as_file('/Users/surenderpal/Projects/Ads-Manager/Screenshots/amazon1.png')
print('screenshot captured!!!')