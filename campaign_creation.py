from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button/div[text()='"+type+"']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-adgTargetSup-next']"))).click()
    time.sleep(3)

def SelectTargeting(AdGroupName,Behavior,Brands,Category,Location_Group): # AdGroupName, Behavior, Brands, Category, Location_Group
    
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adgroup-name']"))).clear() # clear Adgroup Name
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='adgroup-name']"))).send_keys(AdGroupName) # enter Ad Group Name
    # -------Behavior-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Behavior) #click on Audience
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '"+Behavior+"')]"))).click() #Millennials
    time.sleep(2)
    # -------Brands-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Brands) #click on Audience
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'"+Brands+"')]"))).click() # Banana Republic
    time.sleep(2)
    # -------Category-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Category')]"))).click() #click on link
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Category) #click on Category
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'active')]//li[contains(text(), '"+Category+"')]"))).click()
    time.sleep(2)                                                                                                           

    # -------Location Group -------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Location_Group) #click on Location_Group
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'glyphicon-chevron-right')]"))).click() #click on right navigation bar
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Location Group')]"))).click() #click on link
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'active')]//li[contains(text(), '"+Location_Group+"')]"))).click()
    time.sleep(5)

# ========================================Exclude Targeting=============================


def ExcludeTargeting(Behavior,Brands,Category,Location_Group): # Behavior,Brands,Category,Location_Grou
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='audience-fields']/section/a[@class='show-exclude-fields' and contains(text(), 'Exclude Audiences')]"))).click() # click on Exclude link
    # -------Behavior-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Behavior) #value sent to Behavior
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='btn-gtAutocomplete-BehaviorTab']/a[contains(text(), 'Behavior')]"))).click() #click on behavior tab
    time.sleep(1)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(),'"+Behavior+"')]"))).click() # Passed Behavior Dynamic Value i.e. Millennials
    time.sleep(2)
    # # -------Brands-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear on input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Brands) #value send to Audience
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='btn-gtAutocomplete-BrandTab']/a[contains(text(), 'Brand')]"))).click() #click on brands tab
    time.sleep(1)    
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(),'"+Brands+"')]"))).click() # Passed Behavior Dynamic Value i.e. Banana Republic
    time.sleep(2)
    # # # -------Category-------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear on input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Category) #value send to Category
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='btn-gtAutocomplete-CategoryTab']/a[contains(text(), 'Category')]"))).click() #click on category tab
    time.sleep(1)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(),'"+Category+"')]"))).click()
    time.sleep(2)                                                                                                           

    # -------Location Group -------------------
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear on input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[1]/div/gt-autocomplete/div/div/input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Location_Group) #value sent to Location_Group
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='btn-gtAutocomplete-Location GroupTab']/a[contains(text(), 'Location Group')]"))).click() #click on Location_Group tab
    time.sleep(1)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(),'"+Location_Group+"')]"))).click()
    time.sleep(2)

def AdditionalLocationFilter(state,DMA,ZIP): #state, DMA, ZIP
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select state, DMA, or zipcode']"))).click() # Additional location fileter.
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select state, DMA, or zipcode']"))).clear() 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select state, DMA, or zipcode']"))).send_keys(state) #entered state value 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='btn-gtAutocomplete-StateTab']"))).click() #click on State
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[contains(text(), '"+state+"')]"))).click() #clicked on state elelment
    time.sleep(4)                                                         
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select state, DMA, or zipcode']"))).clear()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select state, DMA, or zipcode']"))).send_keys(DMA) #entered DMA value
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='btn-gtAutocomplete-DMATab']"))).click()  #click on DMA tab
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[contains(text(), '"+DMA+"')]"))).click() #clicked on DMA elelment
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select state, DMA, or zipcode']"))).clear()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select state, DMA, or zipcode']"))).send_keys(ZIP) # entered zip 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='btn-gtAutocomplete-ZIP CodeTab']"))).click() #click on zip tab
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'active')]/li[contains(text(), '"+ZIP+"')]"))).click() #click on zip element
    
def demographics():
    # driver.execute_script("")
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-selectAllDemographics']").click() #demographic unchecked
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-genderMale']").click()
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-genderFemale']").click()


Login('gt.surender@protonmail.com','Groundtruth@9')
NewCampaign('Automated campaign')
TargetingTactics()
DeviceType('CTV') # Pass Mobile or CTV
SelectTargeting('Automation@@','Millennials','Banana Republic','Potato Growers','French') # Pass AdGroupName, Behavior, Brands, Category, Location_Group
ExcludeTargeting('Millennials','Banana Republic','Potato Growers','French')
AdditionalLocationFilter('Minnesota','Butte-Bozeman, MT','11')
# demographics()
time.sleep(5)
driver.close()

# //a[contains(@class, 'show-exclude-fields')]
