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

# ======Tenant Dashboard selection===========
# ----selecing Tenant from tenant Dashboard

def select_tenant():
    driver.find_element_by_xpath("//label[text()='Tenant']/..//span[@class='dropdown-title ng-binding']").click()
    time.sleep(3)
    tenantTextbox = driver.find_element_by_xpath("//input[@id='search-dropdown-list-Tenant']")
    tenantTextbox.send_keys('#DelCastillo')
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='Tenant-0']").click()
    time.sleep(5)


# ----selecing Organization from tenant Dashboard
def select_organization():
    driver.find_element_by_xpath("//label[text()='Organization']/..//span[@class='dropdown-title ng-binding']").click()
    time.sleep(3)
    orgTextbox=driver.find_element_by_xpath("//input[@id='search-dropdown-list-Organization']")
    orgTextbox.send_keys('DelCastillo')
    time.sleep(3)
    driver.find_element_by_xpath("//input[@id='Organization-0']").click() #//input[@id='Organization-0']
    time.sleep(5)

# ----selecing account from tenant Dashboard
def select_account():
    driver.find_element_by_xpath("//label[text()='Account']/..//span[@class='dropdown-title ng-binding']").click()
    time.sleep(3)
    actTextbox=driver.find_element_by_xpath("//input[@id='search-dropdown-list-Account']")
    actTextbox.send_keys('Del Castillo Agency')
    time.sleep(3)
    driver.find_element_by_xpath("//input[@id='Account-0']").click()
    time.sleep(3)

# ----selecing Tenant from tenant Dashboard

def select_tenant1():
    driver.find_element_by_xpath("//label[text()='Tenant']/..//span[@class='dropdown-title ng-binding']").click()
    time.sleep(3)
    tenantTextbox = driver.find_element_by_xpath("//input[@id='search-dropdown-list-Tenant']")
    tenantTextbox.send_keys('#GatewayFantasticSams')
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='Tenant-0']").click()
    time.sleep(5)


# ---search Ads Manager(ribbon search bar)---
def universal_search():
    ribbon_search=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".new-search-box-container #inp-base-searchbox-new")))
    ribbon_search.click()
    driver.find_element_by_xpath("//input[@id='inp-base-searchbox-new']").send_keys('Test',Keys.RETURN)
    time.sleep(5)

# logout from Ads manager-----
def logout():
    driver.find_element_by_xpath("//button[@id='btn-userOptions-userOptionsMenuToggle']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//ul/li/a[text()='Sign Out']").click()
    time.sleep(4)

def live_to_date():
    driver.find_element_by_xpath("//input[@name='daterange']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@name='daterangepicker_start']").clear()  #From Date range cleared
    driver.find_element_by_xpath("//input[@name='daterangepicker_start']").send_keys('2020-12-31') #From Date range entered value
    time.sleep(3)
    driver.find_element_by_xpath("//input[@name='daterangepicker_end']").clear()    #To Date range cleared
    driver.find_element_by_xpath("//input[@name='daterangepicker_end']").send_keys('2021-10-29') #To Date range entered value
    time.sleep(3)
    driver.find_element_by_xpath("//button[@class='applyBtn btn-sm btn-success']").click()
    time.sleep(5)
    # From.click()
def pending_campaigns():
    driver.find_element_by_xpath("//button[@id='btn-tenantDash-filterPending']").click()
    time.sleep(4)
def active_campaigns():
    driver.find_element_by_xpath("//button[@id='btn-tenantDash-filterActive']").click()
    time.sleep(4)   
def paused_campaigns():
    driver.find_element_by_xpath("//button[@id='btn-tenantDash-filterPaused']").click()
    time.sleep(4)  
def expired_campaigns():
    driver.find_element_by_xpath("//button[@id='btn-tenantDash-filterExpired']").click()
    time.sleep(4)    
def tenantDashSearchCampaign():
    driver.find_element_by_xpath("//input[@id='inp-tenantDash-searchCampaign']").clear()
    driver.find_element_by_xpath("//input[@id='inp-tenantDash-searchCampaign']").send_keys('test')
    time.sleep(5)
def columnPicker():
    driver.find_element_by_xpath("//button[@id='btn-cm-columnPicker']").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,".//div[@id='modal--column-picker']"))).click()
    ec = driver.find_elements_by_xpath(".//input[contains(@id, 'inp-columnPickerModal') and not(@disabled)]")
    for enabledCheckbox in ec:
        enabledCheckbox.click()
    time.sleep(3)
# ---calling functions-----   
loginAdsManager()

# live_to_date()
# pending_campaigns()
# active_campaigns()
# paused_campaigns()
# expired_campaigns()
# tenantDashSearchCampaign()
columnPicker()

# select_tenant()
# select_organization()
# select_account()
# select_tenant1()
# universal_search()
# logout()
driver.close()  #closing browser
