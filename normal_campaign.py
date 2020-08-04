from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("http://ads-release-3-13-np.groundtruth.com/")

class Login:
    def Alogin(self,username,password):
        driver.maximize_window()
        email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
        email.send_keys(username)
        pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
        pwd.send_keys(password)
        driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]').click()
        time.sleep(3)
L=Login()
L.Alogin('gt.surender@protonmail.com','Groundtruth@9')


# class CampaignDashboard:

def StatusFilter():
    driver.find_element_by_id('btn-campDash-filterAll').click() #All filter
    time.sleep(2)
    driver.find_element_by_id('btn-campDash-filterPending').click() #penging filter
    time.sleep(2)
    driver.find_element_by_id('btn-campDash-filterActive').click() #Active filter
    time.sleep(2)
    driver.find_element_by_id('btn-campDash-filterPaused').click() #paused filter
    time.sleep(2)
    driver.find_element_by_id('btn-campDash-filterExpired').click() #Expired filter
    time.sleep(2)

def Pagination():
    select_pag=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@ng-change='paginateData()']")))) #pagination link
    select_pag.select_by_visible_text('10')
    time.sleep(2)
    select_pag.select_by_visible_text('25')
    time.sleep(2)
    select_pag.select_by_visible_text('50')
    time.sleep(2)

def SearchCampaign():
    driver.find_element_by_id('inp-campDash-searchCampaign').send_keys('Automation')
    driver.find_element_by_xpath("//div[@id='tableHeader-column-id']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-name']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-status']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-pacing']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-spends_spent']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-spends_daily_spent']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-totalBudget']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-timeframe_remain']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-salesforceNumber']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-timeframe_start_string']/a[@ng-click='sort(item.field, true)']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='tableHeader-column-timeframe_end_string']/a[@ng-click='sort(item.field, true)']").click()    



# c=CampaignDashboard
StatusFilter()
Pagination()
SearchCampaign()





