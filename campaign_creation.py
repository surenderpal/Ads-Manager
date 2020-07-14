from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
# driver=webdriver.Firefox()
driver.get("http://ads-release-3-13-np.groundtruth.com/")
def Login(username,password):
    email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
    email.send_keys(username)
    pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
    pwd.send_keys(password)
    driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]').click()
    time.sleep(3)

def NewCampaign(name):
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-campDash-newCampaign']"))).click() #clicked on new campaign
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='campaignNameField']"))).send_keys(name) #campaign name
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='adgroup-budget']"))).click() #adgroup budget
    
    #====for campaign budget enter budget in the text box================ 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='campaign-budget']"))).click() #campaign budget
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='budgetField']"))).send_keys('5') # $ entered in campaign budget
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-campaignCreateModal-submit']"))).click() #save button
    time.sleep(2)

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
def Targeting(): #Behavior, Brands, Category, Location Group 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adgroup-name']"))).clear() # clear Adgroup Name
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adgroup-name']"))).send_keys('Automation@@') # entered input value
    # -------Behavior-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys("Millennials") #click on Audience
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text()='Behavior')]"))).click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Millennials')]"))).click()
    time.sleep(10)
    # -------Brands-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys("KFC") #click on Audience
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text()='Brand')]"))).click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'KFC')]"))).click()
    time.sleep(10)
    # -------Category-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys("Potato Growers") #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text()='Category')]"))).click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Potato Growers')]"))).click()
    time.sleep(10)
    # -------Location Group -------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys("French") #click on Audience
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text()='Location Group')]"))).click()    
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'French')]"))).click()
    time.sleep(20)

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
# driver.close()

    LookAlike=driver.find_element_by_xpath("//input[@id='inp-adGroupTargetingAud-lookalikeAudScale']").is_selected() #Include lookalikes to increas sales
    print("Default Include lookalikes to increase scale:",LookAlike)
    
    driveToDest=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-measurementList']").is_selected() #Drive to Destination radio button
    print("Select real world Drive-To locations (i.e. stores, restaurants) to measure foot traffic visitation:",driveToDest)
    
    NoDriveTo=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-measurementNational']").is_selected() # No Drive-To location, conversion will occur online
    print("No Drive-To location, conversion will occur online:",NoDriveTo)
    
    demographics=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-selectAllDemographics']").is_selected()
    print("Default Demographics checkbox is checked:",demographics)
    
    DeviceTageting=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-toggleAllTechnographics']").is_selected()
    print('Default Device Targeting:', DeviceTageting)

    delivery=driver.find_element_by_xpath("//input[@value='delivery']").is_selected() #delivery
    print('Default Delivery is selected:',delivery)
    
    ele=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-optimizationGoal0']").is_selected() #click optimization starategy
    print("Default click is selected:",ele)

    SAR=driver.find_element_by_xpath("//input[@value='sar']").is_selected() #SAR
    print("Default SAR is selected:",SAR)
    
    conversion=driver.find_element_by_xpath("//input[@value='conversion']").is_selected() #SAR
    print("Default SAR is selected:",conversion)
    
    Auto=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-optimizationAuto0']").is_selected()
    print("Default Optimization Strategy is auto selected:",Auto)
    
    # driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-optimizationAuto0']").click()  #unchecked Auto 
    # driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-optimizationAuto0']").send_keys(0.2) #passed the values into the CTR Threshold
    
    PubCategory=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-selectAllPublisherCats']").is_selected()
    print("Default Publisher Category is selected:",PubCategory)
    
    BuildAudience=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-buildAudience']").is_selected()
    print("Default Build custom audience for remessaging users who see your ad:",BuildAudience)
    #---------------