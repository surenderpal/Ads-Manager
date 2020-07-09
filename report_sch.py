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
        print('report Dashboard is opened')


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
        print('All reports columns are sorted!!')


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
    print('All Report filtered based on status')
def pagination():
        # time.sleep(5)
        # flag=driver.find_element_by_xpath("//a[@id='btn-baseFooter-privacyPolicy']")
        # driver.execute_script("arguments[0].scrollIntoView;",flag)
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        print('scrolling the windows till the bottom of the page')
        # driver.find_element_by_xpath("//select[@class='jss263']").click()
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='jss263']"))).click()
        # driver.find_element_by_xpath("//select[@class='jss263']").click()          #clicked on drop-down for selecting no of records
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
        print('Pagination is tested')


def actions():
        time.sleep(5)
        driver.find_element_by_xpath("//*[@class='MuiButtonBase-root MuiIconButton-root jss249']").click() #clicked on gear icon
        # driver.find_element_by_xpath("//ul/li[text()='Edit' and @role='menuitem']").click()     #clicked on edit 
        # driver.find_element_by_xpath("//ul/li[text()='Pause' and @role='menuitem']").click()      #clicked on Pause 
        # driver.find_element_by_xpath("//ul/li[text()='Resume' and @role='menuitem']").click()     #clicked on Resume
        # driver.find_element_by_xpath("//ul/li[text()='Delete' and @role='menuitem']").click()     #clicked on Delete
        time.sleep(2)
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Delete']"))).click()  #click on Delete button on dialog box
        # driver.find_element_by_xpath("//span[text()='Delete']").click()                         #click on Delete button on dialog box
        # driver.find_element_by_xpath("//span[text()='Cancel']").click()                         #click on Cancel button on dialog box
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cancel']"))).click()  #click on Cancel button on dialog box
        time.sleep(2)
        # print("clicked to pause the report")
        # driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiIconButton-root jss1099']").click() #clicked on back button
        # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root jss1099']"))).click()
        time.sleep(4)
        # driver.find_element_by_xpath("//*[@class='MuiButtonBase-root MuiIconButton-root jss249']").click() #clicked on gear icon
        # driver.find_element_by_xpath("//ul/li[text()='Pause' and @role='menuitem']").click()     #clicked on edit 
        print('clicked on gear icon and selected the desired goal')
        time.sleep(4)

def CreateReport():
        driver.find_element_by_xpath("//button/span[text()='Create Report']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//label[text()='Report Name']/../../div//input").send_keys("Welcome to reports") #report name
        # driver.find_element_by_xpath("//label[text()='Report Type']/../../div//input").click() # report type
        # driver.find_element_by_xpath("//input[@value='Location']").click()              #dropdown location value selected
        # driver.find_element_by_xpath("//input[@id='mui-autocomplete-7539']").send_keys("Location")              #dropdown Product value selected 
        # driver.find_element_by_xpath("//input[@value='Daily Trend']").click()           #dropdown Daily Trend value selected         
        driver.find_element_by_xpath("gt-report-scheduler-create > div > div[class*='sc-'] > div[class*='sc-'] > div:nth-child(1) > div > div > input").click()
        # driver.find_element_by_xpath("").click()
        # driver.find_element_by_xpath("").click()
        # driver.find_element_by_xpath("").click()
        # driver.find_element_by_xpath("").click()
        # driver.find_element_by_xpath("").click()
        # driver.find_element_by_xpath("").click()
        # driver.find_element_by_xpath("").click()
        time.sleep(5)


OpenReporScheduler()
CreateReport()
# reportFilter_SearchReports() 
# ReportsColumnSort()
# pagination()
# actions()
driver.close()