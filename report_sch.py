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
        hamburger = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu")))
        hamburger.click()
        reports = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-reportScheduler")))
        reports.click()
        time.sleep(2)


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


def reportFilter_SearchReports():
    time.sleep(2)
    driver.find_element_by_xpath("//button/span[text()='Pending']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button/span[text()='Active']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button/span[text()='Paused']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button/span[text()='Expired']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button/span[text()='All']").click()
    time.sleep(2)
    # driver.find_element_by_xpath("//input[@placeholder='Search Reports']").send_keys("CBD=FALSE")


def pagination():
    flag=driver.find_element_by_xpath("//a[@id='btn-baseFooter-privacyPolicy']")
    driver.execute_script("arguments[0].scrollIntoView;",flag)
    print('scrolling the windows@@')
    driver.find_element_by_xpath("//select[@class='jss263']").click()
    driver.find_element_by_xpath("//option[@value='25']").click()
    driver.find_element_by_xpath("//span[@class='copyright']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//option[@value='15']").click()
    driver.find_element_by_xpath("//span[@class='copyright']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//option[@value='10']").click()
    driver.find_element_by_xpath("//span[@class='copyright']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[@class='MuiButton-label' and text()='>']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[@class='MuiButton-label' and text()='<']").click()
    time.sleep(2)


def actions():
        driver.find_element_by_xpath("//*[@class='MuiButtonBase-root MuiIconButton-root jss249']").click() #clicked on gear icon
        # driver.find_element_by_xpath("//ul/li[text()='Edit' and @role='menuitem']").click()     #clicked on edit 
        driver.find_element_by_xpath("//ul/li[text()='Pause' and @role='menuitem']").click()     #clicked on Pause 
        time.sleep(8)
        # driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiIconButton-root jss1099']").click() #clicked on back button
        # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root jss1099']"))).click()
        time.sleep(4)
        driver.find_element_by_xpath("//*[@class='MuiButtonBase-root MuiIconButton-root jss249']").click() #clicked on gear icon
        driver.find_element_by_xpath("//ul/li[text()='Pause' and @role='menuitem']").click()     #clicked on edit 
        time.sleep(4)
OpenReporScheduler()
# reportFilter_SearchReports() 
# ReportsColumnSort()
# pagination()
actions()
time.sleep(2)
driver.close()