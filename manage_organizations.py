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
loginAdsManager()
def NewOrg_Account():
    # ---clicking on hamburger menu----
    hamburger = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu")))
    hamburger.click()
    # ----selecting  Manage Organization from hamburger------
    org = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-manageOrg")))
    org.click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-orgList-newOrg']"))).click() #org model opens
    orgName=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='inp-newOrgModal-companyName']"))) #selects the org text box
    orgName.send_keys("staging-3.1") #enters the value in the text box.
    driver.find_element_by_xpath("//button[@id='btn-newOrgModal-save']").click()
    name=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='inp-newAccountModal-name']")))
    name.send_keys('Test@123')
    Advertiser_Domain=driver.find_element_by_xpath("//input[@id='inp-newAccountModal-adomain']") #advertiser Domain
    Advertiser_Domain.send_keys("GroundTruth.com")                                               #Value entered
    driver.find_element_by_xpath("//select[@id='inp-newAccountModal-countryCode']").click()      #Market dropdown clicked
    driver.find_element_by_xpath("//select/option[@value='string:GB']").click()                  #Market dropdown value selected
    driver.find_element_by_xpath("//select[@id='inp-newAccountModal-timezone']").click()         #Timezone dropdown clicked
    driver.find_element_by_xpath("//select/option[@value='string:Europe/London']").click()       #Timezone dropdown value selected
    driver.find_element_by_xpath("//select[@id='inp-newAccountModal-distanceUnit']").click()     #Distance Unit clicked
    driver.find_element_by_xpath("//select/option[@value='string:miles']").click()               #Distance Value selected
    driver.find_element_by_xpath("//select[@id='inp-newAccountModal-currency']").click()         #Currency dropdown 
    driver.find_element_by_xpath("//select/option[@value='string:USD']").click()                 #Currency dropdown value selected: USD
    driver.find_element_by_xpath("//select[@id='inp-newAccountModal-language']").click()         #Language dropdown
    driver.find_element_by_xpath("//select/option[text()='English']").click()
NewOrg_Account()




time.sleep(5)
driver.close()
