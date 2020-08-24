import openpyxl
import XLUtils
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
path="/Users/surenderpal/Downloads/Login.xlsx"

driver.get('https://ads-release-3-13-np.groundtruth.com/')
# driver.maximize_window()
rows=XLUtils.getRowCounnt(path,'GT')
for r in range(2,rows+1):
    username=XLUtils.readData(path,'GT',r,1)
    password=XLUtils.readData(path,'GT',r,2)

    time.sleep(2)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("//button[@id='btn-signin-signIn']").click()
    time.sleep(5)
    
    if driver.current_url!='https://ads-release-3-13-np.groundtruth.com/login?error=Invalid+email+or+password':
        print('Test Passed')
        XLUtils.writeData(path,'GT',r,3,'Pass')

        actions=ActionChains(driver)
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.ID,"btn-userOptions-userOptionsMenuToggle"))).click()
        profile=driver.find_element_by_link_text('Profile')
        Help=driver.find_element_by_link_text('Help')
        singOut=driver.find_element_by_link_text('Sign Out')
        actions.move_to_element(profile).move_to_element(Help).move_to_element(singOut).click().perform()
    else:
        print('Test Failed!!')
        XLUtils.writeData(path,'GT',r,3,'Failed')
        driver.refresh()
        continue
driver.close()