from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("http://ads-release-3-12-np.groundtruth.com/")

def loginAdsManager():
    # driver=webdriver.Chrome()
    # driver.get("http://ads-release-3-12-np.groundtruth.com/")
    time.sleep(2)
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


    # L=Login('http://ads-release-3-12-np.groundtruth.com','surender.pal@groundtruth.com','Surenderpal@1991')

# ---search Ads Manager(ribbon search bar)---
def universal_search():
    ribbon_search=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".new-search-box-container #inp-base-searchbox-new")))
    ribbon_search.click()
    driver.find_element_by_xpath("//input[@id='inp-base-searchbox-new']").send_keys('Test',Keys.RETURN)

loginAdsManager()
# universal_search()
#tenant=WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.XPATH,'.//label[text()="Tenant”]/..//span[@class="dropdown-title ng-binding"]'))
#tenant.click()
# time.sleep(5)
driver.find_element_by_xpath("//label[text()='Tenant']/..//span[@class='dropdown-title ng-binding']").click()
time.sleep(3)
tenantTextbox = driver.find_element_by_xpath(".//input[@id='search-dropdown-list-Tenant']")
tenantTextbox.send_keys('#DelCastillo')
time.sleep(2)
driver.find_element_by_xpath("//input[@name='Tenant-24556']").click()
time.sleep(5)

driver.close()  #closing browser
