from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
# r=random(range(100))
# driver=webdriver.Firefox()
driver.get("http://ads-release-3-13-np.groundtruth.com/")
def Login(username,password):
    # driver.maximize_window()
    email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
    email.send_keys(username)
    pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
    pwd.send_keys(password)
    driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]').click()
    time.sleep(3)


def NewCampaign(name):
    print(driver.title)
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-campDash-newCampaign']"))).click() #clicked on new campaign
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='campaignNameField']"))).send_keys(name) #campaign name
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='adgroup-budget']"))).click() #adgroup budget
    AdGroup=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-createCampModal-budgetAdgLevel']"))).is_selected()
    print("Default Ad group budgets. Set up an ad group specific budget for each targeting tactic:",AdGroup)
#====for campaign budget enter budget in the text box================ 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='campaign-budget']"))).click() #campaign budget
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='budgetField']"))).send_keys('50') # $ entered in campaign budget
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
# -------Behavior-------------------                                        //input[contains(@placeholder, 'Select a brand')]
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Behavior) #click on Audience
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '"+Behavior+"')]"))).click() #Millennials
    time.sleep(2)
#-------Brands-------------------
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
    
    driver.find_element(By.LINK_TEXT, 'Add new location group').click() #new tab location Manager
    handles=driver.window_handles
    driver.switch_to.window(handles[1])
    print(driver.title) #GT Location Manager, GT Ads Manager
# perfomed operation on Location manager
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='vm.openCreateLocationGroupModal()']"))).click() #click on new location group
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='locationGroupName']"))).send_keys('Automation') # L G Name
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='locationGroupDescription']"))).send_keys('Description') # L G Description
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='vm.save()']"))).click() # click on continue button
    time.sleep(2)
    driver.close()
    driver.switch_to.window(handles[0])
# # perfomed operation on Location manager

    # # -------Location Group -------------------
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).click() #click on Input box
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).clear() #clear input box
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']"))).send_keys(Location_Group) #click on Location_Group
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'glyphicon-chevron-right')]"))).click() #click on right navigation bar
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Location Group')]"))).click() #click on link
    # time.sleep(4)
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'active')]//li[contains(text(), '"+Location_Group+"')]"))).click()
    # time.sleep(2)
    lookalike=driver.find_element_by_xpath("//input[@id='inp-adGroupTargetingAud-lookalikeAudScale']").is_selected() #lookalike audience
    print('Default Include lookalikes to increase scale:',lookalike)
# lookalike audience to increase sales

    driver.find_element_by_xpath("//input[@id='inp-adGroupTargetingAud-lookalikeAudScale']").click() #click on the look alike checkbox

    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inp-adGroupTargetingAud-selectedLookalikeAud")))) #selection box
    select.select_by_visible_text('2x of original audience') #value
    time.sleep(1)
    select.select_by_visible_text('4x of original audience') #value
    time.sleep(1)
    select.select_by_visible_text('6x of original audience') #value
    time.sleep(1)
    select.select_by_visible_text('10x of original audience') #value
    time.sleep(1)
    select.select_by_visible_text('4x of original audience')  #value



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
    # -----Value entered using Input box
    # driver.execute_script("window.scrollTo(0, 1000)") #scroll by pixel
    flag=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[@id='location-filter']")))
    driver.execute_script("arguments[0].scrollIntoView();",flag)
    # driver.find_element_by_xpath("//li[contains(text(), 'Drive-To Locations')]").click()
    driver.execute_script("window.scrollBy(0,1000)","")

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
    ## ===Vaule entered or file passed
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='bulk-location-icon']"))).click() #click on Bulk location upload 
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download template here')]"))).click() #download template
    # apdLoc=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-superformModal-appendData']"))).is_selected() #click on append
    # print('Default Append to existing location filters:',apdLoc)
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-superformModal-appendData']"))).click() #click on append    
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='btn-superformModal-uploadFile']"))).click() #clicked on browse button
    # time.sleep(4)
    # Geocoder=driver.find_element_by_xpath("//*[@id='btn-superformModal-uploadFile']/input")
    # Geocoder.send_key("/Users/surenderpal/Downloads/Geotarget.xlsx") #upload file 


def driveToDesti(Brand,Location_group): #brand, Location_group
    flag=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//section[@id='measurements']")))
    driver.execute_script("arguments[0].scrollIntoView();",flag)
    NDrveToLoc=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-measurementNational']").is_selected()
    print('Default Select real world Drive-To locations (i.e. stores, restaurants) to measure foot traffic visitation:',NDrveToLoc)
    drveToLoc=driver.find_element_by_xpath("//input[@id='inp-adgTargetSup-measurementList']").is_selected()
    print('Default Select real world Drive-To locations (i.e. stores, restaurants) to measure foot traffic visitation:',drveToLoc)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-adgTargetSup-measurementList']"))).click()
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select a GroundTruth brand or your custom location group']"))).click() # click on the Drive to location

    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select a GroundTruth brand or your custom location group']"))).clear() #clear
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select a GroundTruth brand or your custom location group']"))).send_keys(Brand) #sent keys Brand 
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='btn-gtAutocomplete-BrandTab']"))).click() #click on the Brand tab
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(), '"+Brand+"')]"))).click() # click on the element

    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select a GroundTruth brand or your custom location group']"))).clear() #clear
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search and select a GroundTruth brand or your custom location group']"))).send_keys(Location_group) #send name Location_group
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@id='btn-gtAutocomplete-Location GroupTab']"))).click()    #click on the Location group
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(), '"+Location_group+"')]"))).click() # click on the element
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-adgTargetSup-next']"))).click() #next button

def VastCreative(name,VastTagURL,ApiType,ExtTracker1,ExtTracker2,ClkThrUrl): #name,VastTagURL,ApiType,ExtTracker,ClkThrUrl
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "btn-adgCreatives-newCreative"))).click() #clicked on new creative
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "inp-creativesModal-creativeName"))).clear() #clear creative name
    # name=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "inp-creativesModal-creativeName"))).get_attribute("ng-model") #getting the name of the creative.
    # print("Default Vast Tag name:",name)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "inp-creativesModal-creativeName"))).send_keys(name) #send key to the name   
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "inp-creativeModalVideo-vastField"))).clear() # Vast Text Area
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "inp-creativeModalVideo-vastField"))).send_keys(VastTagURL) # vast tag url
    time.sleep(2)
    load=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "btn-creativeModalVideo-Videopload"))).get_property('disabled') #getting the status of the load button
    print('Default behaviour of Load button is:',load)
    # Interstitial button default status and clicked --kirti will tell
    # Interstital=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-model='creativeInterstitial']"))).is_selected() #Interstital status
    # print("Default Interstitial is:",Interstital)
    #WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, ".//div[@id='modal--adgroup-new-creative']//div[text()='Interstitial']"))).click() #Interstital clicked
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "btn-creativeModalVideo-Videopload"))).click() #click on the load button                                                                           
    select=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "inp-creativeModalVideo-apiTypeSelect")))) #selection Box
    select.select_by_visible_text(ApiType) #making api type MPAID2  
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='impressions-urls']"))).click() #click on the external impression text box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='impressions-urls']"))).send_keys(ExtTracker1) # entering value to external impression text box    
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-item']"))).click() #click on the + button
    time.sleep(1)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='impressions-urls']"))).send_keys(ExtTracker2) # entering value to external impression text box    
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-item']"))).click() #click on the + button   
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-creativeModalVideo-clickThroughURLField']"))).click() #click through URL
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-creativeModalVideo-clickThroughURLField']"))).send_keys(ClkThrUrl) #value entered into click through URL
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//ul/li/span[contains(text(),'"+ExtTracker2+"')]/button[@class='remove-item']"))).click() #click on the - button
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-creativesModal-newCreativeSave']"))).click() #save button
    print("Creative Added")
    time.sleep(5)

    # print('Default Impression Frequency Cap',FrequencyCap)
    #### creative clonned
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@ng-click='cloneCreative(creative)']"))).click() #cloned the creative
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-simpleConfirmModal-confirm']"))).click() #confirmation model clicked
    # print('Creative cloned')
    #### creative delete
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@ng-click='deleteCreative(creative)']"))).click() # delete creative
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-simpleConfirmModal-confirm']"))).click() # cofirmation model
    # print('Creative Deleted')
    #### Pause Creative
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@ng-click='pauseCreative(creative)']"))).click() #Pause Creative
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-simpleConfirmModal-confirm']"))).click() # cofirmation model
    # print('Creative Paused')
    ####  Creative Opened
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@ng-click='openCreativeModal(creative)']"))).click() #Open Creative
    # print('Creative Opened')
    # time.sleep(2)
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-creativesModal-newCreativeCancel']"))).click() # cancel button
    #### Creative display
    # parentGUID=driver.current_window_handle #return hash key of parent window(Ads Manager)

    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a/i[@class='glyphicon glyphicon-picture creative-action-btn']"))).click() #creative action button or Doc data link
    handles=driver.window_handles
    driver.switch_to.window(handles[1])
    print(driver.title)
    print("Doc Data Displayed:",driver.current_url)
    driver.close()
    driver.switch_to.window(handles[0])            
    FreqCap=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-change='frequencyCappingChange(creative)']"))).is_selected() #Default Frequency cap
    print('Default Impression Frequency Cap:',FreqCap)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-change='frequencyCappingChange(creative)']"))).click() #Frequency cap
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-disabled='creative.frequencyUnlimited']"))).send_keys(10) #impresion cap
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-model='creative.freqCapDuration']"))).clear()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-model='creative.freqCapDuration']"))).send_keys(5) # Imp cap Hour
    time.sleep(3)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-adgTargetSup-creativesTabNext']"))).click() #click on Next button


def BudgetNschedule(Bid_type,BidPrice,SDate,EDAte,DayParting): #Bid_type, BidPrice, SDate,EDAte, DayParting 
    select=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='inp-adgTargetSup-adgBidType']"))))
    select.select_by_visible_text(Bid_type) #Bid_type
    print('Bid Type Selected:',Bid_type)
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-adgTargetSup-bidPrice']"))).clear() #clear bid price
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-adgTargetSup-bidPrice']"))).send_keys(BidPrice) #Bid price
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterange']"))).click() #Timeframe
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_start']"))).clear()
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_start']"))).send_keys(SDate) #daterangepicker_start 
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_end']"))).clear() # clear daterangepicker_end
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_end']"))).send_keys(EDAte) #daterangepicker_end EDAte
    time.sleep(1)
    WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))).click() # click on apply button
    # WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-adgTargetSup-budgetField_0']"))).send_keys("20") #Budget USD
    # WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-adgTargetSup-bidPriceField_0']"))).send_keys(10000) #Impressions
    select=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='inp-adgTargetSup-selectedDaypart']"))))
    select.select_by_visible_text(DayParting) #Day parting 
    time.sleep(2)
# #########
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Sun')]/div//button[contains(text(), '11')]"))).click() # selecting whole Sun row
# ########
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//span[@ng-click='trackingPixelModel()']"))).click()
    time.sleep(4)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-adgTrackingPixelModal-selectAll']"))).click() #click on select all tracking pixel
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-adgTrackingPixelModal-save']"))).click() #click on apply button
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-adgTargetSup-validateTrackingPixel']"))).click() #clicked on Validate All under Advanced settings
    print('Validated under advanced pixels')
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-adgTargetSup-BudSchedSave']"))).click() #click on next button.
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-adgTargetSup-BudSchedSaveLaunch']"))).click() #click on the Save N Launch
    print('Campaign Launched!!!')
    time.sleep(10)

def Reporting():
    WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='btn-cm-summaryTab']"))).click() #Summary tab reporting
    print('click on Summary tab')
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='btn-cm-locationTab']"))).click() # Location tab
    print('click on location tab')
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='btn-cm-audienceTab']"))).click() # Audience tab
    print('click on Audience tab')
    time.sleep(2)
    select=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='cm-selectTableLevel']")))) #Level
    select.select_by_visible_text('Ad Groups') #level Name
    print('selected Ad Groups level')
    select1=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='cm-selectReport']")))) #Report Name
    select1.select_by_visible_text('Category')#Report Name Category
    print('selected report name category')
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterange']"))).click() #Duraion Date Range
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_start']"))).click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_start']"))).clear()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_start']"))).send_keys('2020-08-01') #From Date
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_end']"))).click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_end']"))).clear()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='daterangepicker_end']"))).send_keys('2020-09-21') #From Date
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))).click() #click on apply button
    time.sleep(2) 
    print('selected Duration')
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-cm-toggleChart']"))).click() # Hide Chart
    print('clicked on Hide chart')
####### Matrix --------------------------------    
    # select_mat=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='inp-columnChart-metrics']"))))
    # time.sleep(5)
    # select_mat=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='inp-lineChartMulti-metric1']")))) #Matrix 1
    # select_mat.select_by_visible_text('Visitation Rate (VR)') #impression                            //select[@id='inp-columnChart-metrics']
    # time.sleep(2)
    # select_mat.select_by_visible_text('SAR') #Clicks
    # time.sleep(2)
    # select_mat.select_by_visible_text('CTR') #CTR
    # time.sleep(2)
    # select_mat.select_by_visible_text('Daily Reach') #Daily Reach
    # time.sleep(2)
    # select_mat.select_by_visible_text('Cumulative Reach') #Cumulative Reach
    # time.sleep(2)
    # select_mat.select_by_visible_text('Total Spend') #Total Spend
    # time.sleep(2)
    # select_mat.select_by_visible_text('Secondary Actions') #Secondary Actions
    # time.sleep(2)
    # select_mat.select_by_visible_text('Visits') #Visits
    # time.sleep(2)
    # select_mat.select_by_visible_text('SAR') #SAR
    # time.sleep(2)
    # select_Mat2=Select(WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='inp-lineChartMulti-metric2']")))) #Matrix2    
    # select_Mat2.select_by_visible_text('Impressions') #Impressions
    # time.sleep(2)
    # select_Mat2.select_by_visible_text('Clicks') #Clicks
    # time.sleep(2)
    # select_Mat2.select_by_visible_text('CTR') #CTR
    # time.sleep(2)
    # select_Mat2.select_by_visible_text('Daily Reach') #Daily Reach
    # time.sleep(2)
    # select_Mat2.select_by_visible_text('Cumulative Reach') #Cumulative Reach
    # time.sleep(2)
    # select_Mat2.select_by_visible_text('Total Spend') #Total Spend
    # time.sleep(2)
    # select_Mat2.select_by_visible_text('Secondary Actions') #Secondary Actions
    # time.sleep(2)
    # select_Mat2.select_by_visible_text('Visits') #Visits
    # time.sleep(2)
    # select_Mat2.select_by_visible_text('SAR') #SAR
    # time.sleep(2)
####### Matrix --------------------------------    
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-cm-exportData']"))).click() # Export
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-exportModal-exportLocationReport']"))).click() # Location Reports
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-exportModal-exportTableData']"))).click() #Table Data
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-exportModal-exportReportData']"))).click() #Report Data
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close-modal-btn']"))).click() # report model close button
    print('Export reports downloaded')
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-cm-columnPicker']"))).click() #column picker
    time.sleep(2)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-columnPickerModal-save']"))).click() #column picker apply button
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='multi-select-dropdown']/div[@class='click-element']"))).click() #click on the filter column
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.NAME, "selectedTypes[]"))).click() #click on the filter column
    print('Clicked on the filter column status')
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-cm-tableActionsSearch']"))).send_keys('abcd') # search bar on report page
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-cm-tableActionsSearch']"))).clear() #cleared the input box
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inp-cm-tableActionsSearch']"))).send_keys('Automation@@') # search bar on report page
    time.sleep(2)
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-binding ng-scope']/input[contains(text(),'Active')]"))).click() #
    time.sleep(2)
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, ""))).click() #
    # time.sleep(2) 
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, ""))).click() #
    # time.sleep(2)
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, ""))).click() #
    # time.sleep(2)





def demographics():
    # driver.execute_script("")
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-selectAllDemographics']").click() #demographic unchecked
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-genderMale']").click()
    driver.find_element_by_id("//input[@id='inp-adgTargetSup-genderFemale']").click()


Login('gt.surender@protonmail.com','Groundtruth@9')
NewCampaign('Automated campaign') #+random.randint(0,9)
TargetingTactics()
DeviceType('CTV') # Pass Mobile or CTV
SelectTargeting('Automation@@','Millennials','Banana Republic','Potato Growers','French') # Pass AdGroupName, Behavior, Brands, Category, Location_Group
# ExcludeTargeting('Millennials','Banana Republic','Potato Growers','French')
AdditionalLocationFilter('Minnesota','Butte-Bozeman, MT','11')
driveToDesti('7-Eleven','Volvo') 
''' # ApiType='None','VPAID1','VPAID2','MRAID1','MRAID2','ORMMA' '''
VastCreative('Vast Creative','https://ad.doubleclick.net/ddm/pfadx/N3175.3207085GROUNDTRUTH/B23223750.270292578;sz=0x0;ord=%%TIMESTAMP%%;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;dcmt=text/xml;dc_sdk_apis=[APIFRAMEWORKS];dc_omid_p=[OMIDPARTNER]','MRAID2','https://stackoverflow.com/','https://abcd.com/','https://www.groundtruth.com/')
BudgetNschedule('CPM',22,'2020-07-30','2020-09-30','Happy Hour')
Reporting()
time.sleep(5)
row=driver.find_element_by_id("tableBody-column-id")
actions=ActionChains(driver)
actions.context_click(row).perform()
# actions.double_click(row).perform()
# print('double clicked on row')
# driver.quit()
