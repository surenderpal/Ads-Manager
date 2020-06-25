from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# class Login:
    # def __init__(url,email,pwd):
    #     self.url=url
    #     self.email=email
    #     self.pwd=pwd

def loginAdsManager():
    driver=webdriver.Chrome()
    driver.get("http://ads-release-3-12-np.groundtruth.com/")
    email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
    email.send_keys('surender.pal@groundtruth.com')
    pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
    pwd.send_keys('Surenderpal@1991')

    signInButton=driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]')
    signInButton.click()
    # ---clicking on hamburger menu----
    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu")))
    button.click()
    # ------clicking on Tenant Dashboard
    tenant_dashboard = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-tenant-dashboard")))
    tenant_dashboard.click()

    time.sleep(3)
    driver.close()  #closing browser
# L=Login('http://ads-release-3-12-np.groundtruth.com','surender.pal@groundtruth.com','Surenderpal@1991')
loginAdsManager()