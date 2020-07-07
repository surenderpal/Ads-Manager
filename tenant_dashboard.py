import Ads_login
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
# ======Tenant Dashboard selection===========
# ----selecing Tenant from tenant Dashboard
# driver=webdriver.Chrome()
# driver.get("http://ads-release-3-12-np.groundtruth.com/")
class TenantDashboard(Ads_login.Login):
    """ Ads manager Tenant Dashboard class"""    
    
    def select_tenant(self,tenantName):
        tenant_dashboard = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-tenant-dashboard")))
        tenant_dashboard.click()
        self.driver.find_element_by_xpath("//label[text()='Tenant']/..//span[@class='dropdown-title ng-binding']").click()
        time.sleep(3)
        tenantTextbox = self.driver.find_element_by_xpath("//input[@id='search-dropdown-list-Tenant']")
        tenantTextbox.send_keys(tenantName)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='Tenant-0']").click()
        time.sleep(5)

    # ----selecing Organization from tenant Dashboard
    def select_organization(self,OrgName):
        self.driver.find_element_by_xpath("//label[text()='Organization']/..//span[@class='dropdown-title ng-binding']").click()
        time.sleep(3)
        orgTextbox=self.driver.find_element_by_xpath("//input[@id='search-dropdown-list-Organization']")
        orgTextbox.send_keys(OrgName)
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@id='Organization-0']").click() #//input[@id='Organization-0']
        time.sleep(5)

    # ----selecing account from tenant Dashboard
    def select_account(self,AccountName):
        self.driver.find_element_by_xpath("//label[text()='Account']/..//span[@class='dropdown-title ng-binding']").click()
        time.sleep(3)
        actTextbox=self.driver.find_element_by_xpath("//input[@id='search-dropdown-list-Account']")
        actTextbox.send_keys(AccountName)
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@id='Account-0']").click()
        time.sleep(3)


# TenantDashboard.
t=TenantDashboard()
t.login_ads('surender.pal@groundtruth.com','Surenderpal@1991')
TenantDashboard()
time.sleep(5)
t.select_tenant('Test Tenant')
t.select_organization('SS Tests (Staging)')
t.select_account('SS Tests (Staging)')

