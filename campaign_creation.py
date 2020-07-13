from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("http://ads-release-3-13-np.groundtruth.com/")
def Login(username,password):
    email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
    email.send_keys(username)
    pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
    pwd.send_keys(password)
    driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]').click()
    time.sleep(3)

def NewCampaign(name):
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-campDash-newCampaign']"))).click() #clicked on new campaign
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='campaignNameField']"))).send_keys(name) #campaign name
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='adgroup-budget']"))).click() #adgroup budget
    
    #====for campaign budget enter budget in the text box================ 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='campaign-budget']"))).click() #campaign budget
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='budgetField']"))).send_keys('5') # $ entered in campaign budget
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-campaignCreateModal-submit']"))).click() #save button
    time.sleep(4)

def TargetingTactics(): #TTName--pased name as variable to select TTName
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Target by Location']"))).click()  # Location TTName
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//h4[text()='On Premise Targeting']"))).click() #On Premise
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//h4[text()='Neighborhoods']"))).click() # Neighborhoods 
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div/h4[text()='Geotargets']"))).click() # Geotargets 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Target by Audience']"))).click()  # Audience TTName
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Target by Weather']"))).click()  # Weather TTName
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-adgGoals-next']"))).click()  # Next Button
    time.sleep(5)

def DeviceType(type):
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button/div[text()='Mobile']"))).click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, type))).click()
    time.sleep(3)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-adgTargetSup-next']"))).click()
    time.sleep(3)
'''
for mobile == //button/div[text()='Mobile']"
for ctv== //button/div[text()='CTV']
'''
def Targeting():
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adgroup-name']"))).clear() # clear Adgroup Name
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adgroup-name']"))).send_keys('Automation@@') # entered input value
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys("Millennials") #click on Audience
    driver.find_element_by_xpath("//*[text()='Millennials']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div/li[@class='autocomplete-item ng-binding ng-scope highlighted' and text()= 'Millennial Parents']").click()
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Behavior (100)']"))).send_keys("Millennials") #Behavior
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Behavior (100)']"))).click() #Behavior

def demographics():
    # driver.execute_script("")
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-selectAllDemographics']").click() #demographic unchecked
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-genderMale']").click()
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-genderFemale']").click()


Login('gt.surender@protonmail.com','Groundtruth@9')
NewCampaign('Automated campaign')
TargetingTactics()
DeviceType("//button/div[text()='Mobile']")
Targeting()
# demographics()
driver.close()

