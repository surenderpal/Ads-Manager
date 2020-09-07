from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("http://ads-release-3-12-np.groundtruth.com/")

class Login():
    """ Ads manager login class"""        
    def login_ads(self,username,password):
        email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
        email.send_keys(username)
        pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
        pwd.send_keys(password)
        signInButton=driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]')
        signInButton.click()
        print("{} has been logged in successfully!!".format(username))
        time.sleep(5)
l=Login()
l.login_ads('surender.pal@groundtruth.com','Surenderpal@1991')

class hamburger():
    def tenantDashboard():
        # ---clicking on hamburger menu----
        ham = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu")))
        ham.click()
        # ------clicking on Tenant Dashboard
        t_dashboard = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-tenant-dashboard")))
        t_dashboard.click()

