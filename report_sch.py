from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("http://ads-release-3-12-np.groundtruth.com/")

def login_ads(username,password):
        email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
        email.send_keys(username)
        pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
        pwd.send_keys(password)
        signInButton=driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]')
        signInButton.click()
        print("{} has been logged in successfully!!".format(username))

login_ads('surender.pal@groundtruth.com','Surenderpal@1991')

def OpenReporScheduler():
        hamburger = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu")))
        hamburger.click()
        reports = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-reportScheduler")))
        reports.click()
        time.sleep(2)

OpenReporScheduler()

def ReportsColumnSort():
        driver.find_element_by_xpath("//span[text()='Report Name']").click()            #report's sorting
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='Report Type']").click()            #reports type
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='Created By']").click()             #created by 
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='Creation Date']").click()          #creation date
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='# Recipients']").click()           #Recipients
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='Status']").click()                 #status
        time.sleep(2)
        print('All reports sorting are tested!!')
# ReportsColumnSort()



def reportFilter():
#     pending=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-tenantDash-filterPending']")))
#     pending.click()
    # time.sleep(2)
    Active=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btn-tenantDash-filterActive")))
    Active.click()
    # Paused=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "#btn-tenantDash-filterPaused")))
    # Paused.click()
    # Expired=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "#btn-tenantDash-filterExpired")))
    # Expired.click()
    # driver.find_element_by_xpath("//button[@id='btn-tenantDash-filterPending']").click()
    # print('Sorting by Pending')
    # driver.find_element_by_xpath("//button[@id='btn-tenantDash-filterActive']").click()
    # print('Sorting by Active')
    # driver.find_element_by_xpath("//button[@id='btn-tenantDash-filterPaused']").click()
    # print('Sorting by Paused')
    # driver.find_element_by_xpath("//button[@id='btn-tenantDash-filterExpired']").click()
    # print('Sorting by Expired')

reportFilter()
time.sleep(2)
driver.close()