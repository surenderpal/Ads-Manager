from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager 
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
import re

b_name ='chrome'
if b_name == 'chrome':
    driver=webdriver.Chrome(ChromeDriverManager().install()) #this will install chrome
elif b_name == 'firefox':
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif b_name == 'ie':
    driver=webdriver.Ie(IEDriverManager().install())
elif b_name == 'edge':
    driver=webdriver.Edge(EdgeChromiumDriverManager().install())
elif b_name == 'safari':
    driver=webdriver.Safari()
else:
    print('Please enter the correct browser name'+b_name)
driver.get('https://ads-release-3-16-np.groundtruth.com/')

driver.implicitly_wait(10)

class AdsManager():
    def linksInLoginPage(self,tagname):
        driver.maximize_window()
        links=driver.find_elements(By.TAG_NAME, tagname)
        ttl=driver.title
        print('Total links present on '+ttl+' is:',len(links))
        for link in links:
            print(link.text,link.get_attribute('href'))


    def login(self,username,password):
        textBoxCount=driver.find_elements(By.XPATH, "//input")
        print('Total text box present on login page is:'+str(len(textBoxCount)))
        for input in textBoxCount:
            print(input.get_attribute('name'))
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_id('btn-signin-signIn').click()
        sleep(5)
        if driver.title=='GT Ads Manager':
            print('Login successfull!! to '+ driver.title)
        else:
            print('Please enter valid credentials!!!')
A=AdsManager()
# A.linksInLoginPage('a')
A.login('gt.surender@protonmail.com','Groundtruth@9')

class campaignSetUp():
    '''
    setting up campaign for testing purpose
    '''
    def NewCampaignButton(self):
        '''
        this function will setup new campaign
        '''
        newCampaignButton=driver.find_element(By.XPATH, "//button[@id='btn-campDash-newCampaign']")
        if newCampaignButton.tag_name == 'button':
            driver.find_element(By.XPATH, "//button[@id='btn-campDash-newCampaign']").click()
            print('clicked on new campaign button')
        else:
            print('new campaign button is not found!!')
    def NewCampaignModel(self,CampaignName,categoryName,BudgetType,ModelAction): #campaignAction
        '''
        this function is created by surender pal, it opens the campaign creation model, and fills the form,
        campaignName is the name of campaign that user creates, campaign name can be anything.
        categoryname is the name of category that user selects, user has to select from list,
        BudgetType is the type of budget that user selects. budget can be of two types Ad Group and Campaign level #adgroup, campaign
        BudgetType value="campaign-budget" , value="adgroup-budget" 
        campaignAction is either 'Save' or '×'
        '''
        ToolTipText = '''A budget is the amount of money you want to spend on showing people your ads. 

 Campaign budget is a budget you set once at the campaign level. The campaign budget will be shared across ad groups based on available inventory that each ad group is competing for. Spending will not be evenly divided across all ad groups. 

 Ad group budgets are set for each ad group, when you setup the targeting tactics. This provides more granular budget control but has the risk of under delivery. You also have the option to convert ad group budgets to a single campaign budget after launching the campaign.'''
        actions=ActionChains(driver)
        ModelTitle = driver.find_element(By.XPATH, "//div[@id='modal--create-new-campaign']//div[text()='Create new campaign']") #model title
        labels=driver.find_elements(By.XPATH, "//label['inp-createCampModal']")
        print('*' * 50)
        print('count of labels inside create new campaign model:',len(labels))

        
        if ModelTitle.get_attribute('innerHTML') ==  'Create new campaign':
            print('Passed, Model title!!')
            budgetSetting = 'Budget Setting'
            category = driver.find_element(By.XPATH, "//input[@placeholder='Search and select a category']")
            AdGroupBudgetLabel = driver.find_element(By.XPATH, "//div[@class='radio-wrapper']/label[@for='inp-createCampModal-budgetAdgLevel']").text
            CampaignBudgetLabel = driver.find_element(By.XPATH, "//div[@class='radio-wrapper']/label[@for='inp-createCampModal-budgetCampLevel']").text
            CampaignLabelName = driver.find_element(By.XPATH, "//div[@class='name-field']/label[@for='inp-createCampModal-campName']").get_attribute('innerHTML')
            CategoryLabelName = driver.find_element(By.XPATH, "//label[contains(text(),'Category')]").get_attribute('innerHTML')
            infoInnerText=driver.find_element(By.XPATH, "//label[@class= 'budget-title']/span").get_attribute('uib-popover') #tool tip text
            info=driver.find_element(By.XPATH, "//label[@class='budget-title']/span")# info tool tip
            note = driver.find_element(By.XPATH, '//p').text #Note warning inside campaign budget
 
            if CampaignLabelName == 'Campaign Name':
                print('Passed, Campaign Name Label is correct!!')
                driver.find_element(By.ID, "inp-createCampModal-campName").send_keys(CampaignName) #campaign name 
                if CategoryLabelName == 'Category':
                    print('Passed, Category Name Label is correct!!')
                    if category.get_attribute('placeholder') == 'Search and select a category':
                        print('Passed!!,Placeholder inside Category')
                        category.click()
                        sleep(2)
                        category_li = driver.find_elements(By.XPATH, "//div[@class='gt-autocomplete-dropdown ng-scope']/ul/li")
                        print('#' * 30)
                        print('Count of category:',len(category_li))                        
                        print('categories are listed below:-')
                        for li in category_li:
                            print(li.text)
                        print('#' * 30)
                        driver.find_element(By.XPATH,"//li[contains(text(),'"+categoryName+"')]").send_keys(categoryName)# category name:- Potato Growers
                    else:
                        print('Failed!!,Placeholder inside Category')
                else:
                    print('Failed, Category Name lable is Incorrect') 
            else:
                print('Failed, Campaign Name lable is Incorrect')

            if driver.find_element(By.CLASS_NAME, 'budget-title').text == budgetSetting:
                print('Passed, budget setting label text is correct')
                actions.move_to_element(info).perform()
                if infoInnerText == ToolTipText:
                    print('Passed, info tool tip text is correct')
                    print('Count of radio button available:-',len(driver.find_elements(By.NAME, "budget")))
                    driver.find_element(By.NAME, "budget").is_selected() #default selection
                    print('Is By Default Adgroup selected:-',driver.find_element(By.XPATH, "//input[@value='adgroup-budget']").is_selected())
        
                    budgets = driver.find_elements(By.NAME, "budget")
                    if AdGroupBudgetLabel == 'Ad group budgets. Set up an ad group specific budget for each targeting tactic.':
                        print('Passed, Ad group label is correct')
                    else:
                        print('Failed, Ad group label is incorrect')

                    if CampaignBudgetLabel == 'Campaign budget. Set up one budget for all ad groups associated to this campaign.':
                        print('Passed, Campaign Budget label is correct')
                    else:
                        print('Failed, Campaign Budget label is incorrect')
                    for budget in budgets:
                        print('Type  of Budget options:',budget.get_attribute('value'))
                        if BudgetType == 'adgroup-budget':
                            # driver.find_element(By.ID, "btn-campaignCreateModal-submit").click()
                            pass
                        else:
                            if BudgetType == 'campaign-budget':
                                    driver.find_element_by_xpath("//input[@value='campaign-budget']").click()
                                    note = driver.find_element(By.XPATH, '//p').text #Note warning inside campaign budget
                                    if note == 'Note: Selecting this option does not guarantee even budget distribution amongst each ad group. Once saved, this setting cannot be changed.':
                                        print('Passed, campaign Note!!')
                                        budgetUsdLabel = 'Budget USD'
                                        if budgetUsdLabel == driver.find_element(By.XPATH, "//label[contains(text(),'Budget USD')]").get_attribute('innerHTML'):
                                            print('Passed, Budget USD label is correct')
                                            driver.find_element(By.NAME, "budgetField").clear()
                                            driver.find_element(By.NAME, "budgetField").send_keys('10')
                                        else:
                                            print('Failed, Budget USD label is Incorrect')
                                    else:
                                        print('Failed, campaign Note!!')
                            else:
                                print('Failed, Wrong budget selected!!')
                            break
                    # clientContractLabelName= 'Client Contract / IO Number'
                    # if clientContractLabelName == driver.find_element(By.XPATH, "//label[contains(text(),'Client Contract / IO Number')]").get_attribute('innerHTML'):
                    #     print('Passed, client contract/ IO number is correct!!')
                    #     driver.find_element(By.XPATH,"//input[@id='inp-createCampModal-channelClientIoNumber']").clear()
                    #     driver.find_element(By.XPATH,"//input[@id='inp-createCampModal-channelClientIoNumber']").send_keys('123sdeafsad')
                    # else:
                    #     print('Failed, client contract/ IO number is correct!!')

                    sleep(4)
                    driver.find_element(By.XPATH, "//button/span[contains(text(),'"+ModelAction+"')]").click()
                    print('Performed operation on create new campaign is:',ModelAction)
                else:
                    print('Failed, info tool tip text is Incorrect')
            else:
                print('Failed, budget setting label text is Incorrect')
        else:
            print('Failed, Model title!!')

    def TargettingHeader(self):
        '''
        Targetting tatics header, testing verifying each details
        '''
        print('*'*50)
        print('Targeting tactics page details are below:- ')
        # sleep(5)
        totalLabels = driver.find_elements(By.XPATH, "//div[@class='label' or @class = 'item-type']")
        print('#' * 30)
        print('Labels details are listed below:-')
        print('Count of label on targeting tactics is:',len(totalLabels))
        for lable in totalLabels:
            print(lable.text)
        # print('#' * 30)
        adGroup = driver.find_element(By.XPATH, "//div[contains(text(),'Ad Group')]").text
        if adGroup == 'Ad Group':
            print('Passed Ad group title')
        else:('Failed Ad group title',adGroup)
        h2 = driver.find_element(By.XPATH, "//h2[contains(text(),'New Ad Group')]").text
        if h2 == 'New Ad Group':
            print('Passed,Default Ad Group Name is correct')
        else:
            print('Failed,Default Ad Group Name is:',h2)

        budgetlabel = driver.find_element(By.XPATH, "//div[contains(text(),'Budget')]").text
        if budgetlabel == 'Budget':
            print('Passed, Budget label is correct')
        else:
            print('Passed, Budget label is correct')

        budgetvalue= driver.find_element(By.ID, "contextualHeader-adgroupBudgetValue").text
        print('budgetAmount entered:-',budgetvalue)
        usdLabelnearBudgetValue=driver.find_element(By.XPATH, "//span[@id='contextualHeader-adgroupBudgetUnit']").text
        if usdLabelnearBudgetValue == 'USD':
            print('Passed, USD label near Budget value is correct')
        else:
            print('Failed, USD label near Budget value is Incorrect',usdLabelnearBudgetValue)
        totalSpentLable = driver.find_element(By.XPATH, "//div[contains(text(),'Total Spent')]").text
        if totalSpentLable == 'Total Spent':
            print('Passed, Total Spent label is correct')
        else:
            print('Failed, Total Spent label is Incorrect',totalSpentLable)

        totalSpentvalue = driver.find_element(By.ID, "contextualHeader-adgroupTotalSpentValue").text
        print('Total spent value:',totalSpentvalue)
        usdLabelNearSpentValue = driver.find_element(By.ID, "contextualHeader-adgroupTotalSpentUnit").text

        if usdLabelNearSpentValue == 'USD':
            print('Passed, USD label near total spent value is correct')
        else:
            print('Failed, USD label near total spent value is Incorrect',usdLabelNearSpentValue)
        
        statuslable = driver.find_element(By.XPATH, "//div[contains(text(),'Status')]").text
        if statuslable == 'Status':
            print('Status label is correct')
        else:
            print('Status lable is incorrect',statuslable)


        statusDefaultValue = driver.find_element(By.ID, "contextualHeader-adgroupStatusValue").text
        print('Default value of status is:',statusDefaultValue)
        targettingSectionHeading = driver.find_element(By.XPATH, "//div[@class='targeting-goals-view ng-scope']/h2").text
        if targettingSectionHeading == 'Start building your advertising campaign by selecting one of the following location targeting tactics':
            print('Passed, Targeting tactics heading is correct')
        else:
            print('Failed, Targeting tactics heading is Incorrect',targettingSectionHeading)

        actions=ActionChains(driver)
        info=driver.find_element(By.XPATH, "//div[@class='targeting-goals-view ng-scope']/h2/span")
        actions.move_to_element(info).perform()
        sleep(2)
        if info.get_attribute('uib-popover') == 'Note: you can add other types of tactics to your campaign as you continue through your set up.':
            print('Passed, tooltip under the targeting tactics is correct')
        else:
            print('Failed, tooltip under the targeting tactics is Incorrect',info.get_attribute('uib-popover'))

        noOftactics =  driver.find_elements(By.XPATH, "//div[@class='targeting-goals-view ng-scope']/ul/li")
        print('Count of tactics available is',len(noOftactics))
        print('%' * 50)
        tactics = driver.find_elements(By.XPATH, "//div[@class='goal-label']/h3")
        for tactic in tactics:
            tacticOption= 'Target by Audience' #Location
            tacticOption2 = 'Target by Audience' #Audience,Weather
            if tactic.text == tacticOption: #if tactic name is Location Target by Weather, Target by Audience
                print('Target by Location Paragraph:',driver.find_element(By.XPATH, "//div[@class='goal-label']/p").text)
                tactic.click()
                subTactic= 'On Premise Targeting' # On Premise Targeting,Neighborhoods,Geotargets
                print('Sub tactics count inside Target by Location:',len(driver.find_elements(By.XPATH,"//h4[contains(text(),'')]"))-1)
                driver.find_element(By.XPATH,"//h4[contains(text(),'"+subTactic+"')]").click()
                subtacticPara = driver.find_elements(By.XPATH,"//div[@class='sub-option-text']/p")
                for p in subtacticPara:
                    print(p.text)
                driver.find_element(By.ID,"btn-adgGoals-next").click()
                break
            else:
                driver.find_element(By.XPATH, "//h3[contains(text(),'"+tacticOption2+"')]").click()
                driver.find_element(By.ID,"btn-adgGoals-next").click()
                break       
        tacticParagraph= driver.find_elements(By.XPATH, "//div[@class='goal-label']/p")
        for p in tacticParagraph:
            print(p.text)
    
    def deviceType(self):
        devicetypeheading = driver.find_element(By.XPATH, "//h4[contains(text(),'Device Type')]").text
        devicetypeparagraph = driver.find_element(By.XPATH, "//h6[contains(text(),'Select')]").text
        MobileButton = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root jss33 jss34']")
        nextButton=driver.find_element(By.ID,"btn-adgTargetSup-next")
        if devicetypeheading == 'Device Type':
            print('Passed, Device type heading')
        else:
            print('Failed!')
        if devicetypeparagraph == 'Select the device type you would like to advertise on to reach your desired audience':
            print('Passed, device type paragraph')
        else:
            print('Failed, device type paragraph!!')   
             
        if MobileButton.is_enabled() == True and nextButton.is_enabled() == True:
            MobileIconText = driver.find_element(By.XPATH, "//div[contains(text(),'Mobile')]")
            if MobileIconText.text == 'Mobile':
                print('Passed, Mobile Icon text is correct')
                MobileButton.click()
                nextButton.click()
            else:
                print('Failed, Mobile Icon text is Incorrect')
            print('Passed, clicked on Mobile and next button')
        else:
            print('Either Mobile button or Next button is disabled')
    def LeftHandDetails(self):
        buttons=driver.find_elements(By.XPATH, "//div[contains(@ng-click, 'goToStep')]")
        liInButton = driver.find_elements(By.XPATH, "//li[contains(@ng-click,'goToSection')]")
        print('%'*50)
        print('LeftHand details')
        print()
        print('count of buttons:',len(buttons))
        print('count of li:',len(liInButton))
        for button in buttons:
            print(button.text)
        liInButton = driver.find_elements(By.XPATH, "//li[contains(@ng-click, 'goToSection')]")
        list = ['Behavior / Custom Audience','Location Filter','Drive-To Locations','Demographics','Optimization Strategy','Publisher Categories','Build Audience']
        for i in range(len(list)):
            li=driver.find_element(By.XPATH, "//li[contains(text(),'"+list[i]+"')]")
            li.click()
            sleep(2)
        # ButtonList=['Targeting Goal','Device Type','Target Audience','Ad Creatives','Budget & Schedule'] 
        if driver.find_element(By.XPATH, "//div[contains(text(),'Targeting Goal')]").text == 'Targeting Goal':
            print('Passed, Targeting Goal, Label is correct')
        else:
            print('Failed, Targeting Goal, Label is incorrect')
        
        if driver.find_element(By.XPATH, "//div[contains(text(),'Device Type')]").text == 'Device Type':
            print('Passed, Device Type, Label is correct')
        else:
            print('Failed, Device Type, Label is incorrect')
        if driver.find_element(By.XPATH, "//div[contains(text(),'Target Audience')]").text == 'Target Audience':
            print('Passed, Target Audience, Label is correct')
        else:
            print('Failed, Target Audience, Label is incorrect')
        if driver.find_element(By.XPATH, "//div[contains(text(),'Ad Creatives')]").text == 'Ad Creatives':
            print('Passed, Ad Creatives, Label is correct')
        else:
            print('Failed, Ad Creatives, Label is incorrect')
        if driver.find_element(By.XPATH, "//div[contains(text(),'Budget & Schedule')]").text == 'Budget & Schedule':
            print('Passed, Budget & Schedule, Label is correct')
        else:
            print('Failed, Budget & Schedule, Label is incorrect') 
        if driver.find_element(By.XPATH, "//li[contains(text(),'Behavior / Custom Audience')]").text == 'Behavior / Custom Audience':
            print('Passed, Behavior / Custom Audience, Label is correct')
        else:
            print('Failed, Behavior / Custom Audience, Label is incorrect')
        if driver.find_element(By.XPATH, "//li[contains(text(),'Location Filter')]").text == 'Location Filter':
            print('Passed, Location Filter, Label is correct')
        else:
            print('Failed, Location Filter, Label is incorrect')
        if driver.find_element(By.XPATH, "//li[contains(text(),'Drive-To Locations')]").text == 'Drive-To Locations':
            print('Passed, Drive-To Locations, Label is correct')
        else:
            print('Failed, Drive-To Locations, Label is incorrect')
        if driver.find_element(By.XPATH, "//li[contains(text(),'Demographics')]").text == 'Demographics':
            print('Passed, Demographics, Label is correct')
        else:
            print('Failed, Demographics, Label is incorrect')
        if driver.find_element(By.XPATH, "//li[contains(text(),'Optimization Strategy')]").text == 'Optimization Strategy':
            print('Passed, Optimization Strategy, Label is correct')
        else:
            print('Failed, Optimization Strategy, Label is incorrect')
        if driver.find_element(By.XPATH, "//li[contains(text(),'Publisher Categories')]").text == 'Publisher Categories':
            print('Passed, Publisher Categories, Label is correct')
        else:
            print('Failed, Publisher Categories, Label is incorrect')
        if driver.find_element(By.XPATH, "//li[contains(text(),'Build Audience')]").text == 'Build Audience':
            print('Passed, Build Audience, Label is correct')
        else:
            print('Failed, Build Audience, Label is incorrect')

    def RightHandDetials(self):
        print('%'*50)
        print('RightHand details')
        infoText='Estimates are based on many factors, including past campaign data, location targeting, audience targeting, bid prices, budget, and market data. These numbers are provided to give you an idea of performance for your targeting configuration, but are only estimates and do not guarantee results.'
        estimedReslultLabel = driver.find_element(By.XPATH, "//div[contains(text(), 'Estimated Results')]").text
        if estimedReslultLabel == 'Estimated Results':
            print('Passed, Estimated Results Label is correct')
        else:
            print('Failed, Estimated Results Label is incorrect')
        actions=ActionChains(driver)
        infoIcon= driver.find_element(By.XPATH, "//img[@class='icon-info']")
        actions.move_to_element(infoIcon).perform()
        sleep(2)
        if infoIcon.get_attribute('uib-popover') == infoText:
            print('Passed, Text inside the info Icon is correct')
        else:
            print('Failed, text inside the info icon is incorrect')

        availsTitle = driver.find_elements(By.XPATH, "//div[@class='avails-title']")
        print('Count of Avails title under map:',len(availsTitle))
        for title in availsTitle:
            print(title.text)
        if driver.find_element(By.XPATH, "//div[contains(text(),'Projected Daily Impressions')]").text == 'Projected Daily Impressions':
            print('Passed,Projected Daily Impressions lable is correct')
        else:
            print('Failed,Projected Daily Impressions lable is incorrect')
        if driver.find_element(By.XPATH, "//div[contains(text(),'Audience Daily Reach')]").text == 'Audience Daily Reach':
            print('Passed,Audience Daily Reach label is correct')
        else:
            print('Failed,Audience Daily Reach label is incorrect')
        if driver.find_element(By.XPATH, "//div[contains(text(),'Audience Targeting')]").text == 'Audience Targeting':
            print('Passed,Audience Targeting label is correct')
        else:
            print('Failed, Audience Targeting label is failed!')
    
    def AdGroupHeader(self):
        headerBudgetlabel = driver.find_element(By.XPATH, "//div[contains(text(),'Budget') and @class ='label']").text
        headerTotalSpentlabel=driver.find_element(By.XPATH, "//div[contains(text(),'Total Spent')]").text
        headerStatuslabel = driver.find_element(By.XPATH, "//div[contains(text(),'Status')]").text
        budgetUsdLabel= driver.find_element(By.ID, "contextualHeader-adgroupBudgetUnit").text
        totalSpentUsdLabel= driver.find_element(By.ID, "contextualHeader-adgroupTotalSpentUnit").text
        headerstatusvalue = driver.find_element(By.ID, "contextualHeader-adgroupStatusValue").text

        print('%'*50)
        print('Headers details')
        adGrouplabel = driver.find_element(By.XPATH, "//div[contains(text(),'Ad Group')]").text
        if adGrouplabel == 'Ad Group':
            print('Passed',adGrouplabel,'is correct')
        else:
            print('Failed',adGrouplabel,'is incorrect')
        defaultAdgroupName = driver.find_element(By.XPATH, "//h2[@class='ng-binding']").text
        if defaultAdgroupName == 'New Ad Group':
            print('Passed, Default Ad Group name is,',defaultAdgroupName, 'and it is correct')
        else:
            print('Failed, Default Ad Group name is,',defaultAdgroupName, 'and it is failed')
        allHeaderLabel=driver.find_elements(By.XPATH, "//div[@class='label']")
        
        print('Header label details are listed below:-')
        print('count of label in header:',len(allHeaderLabel))
        for label in allHeaderLabel:
            print(label.text)
        if headerBudgetlabel == 'Budget':
            print('Passed,',headerBudgetlabel,'label is correct')
        else:
            print('Failed,',headerBudgetlabel,'label is incorrect')
        if budgetUsdLabel == 'USD':
           print('Passed,',budgetUsdLabel,'label is correct')
        else:
            print('Failed,',budgetUsdLabel,'label is incorrect') 
        if headerTotalSpentlabel == 'Total Spent':
            print('Passed,',headerTotalSpentlabel,'label is correct')
        else:
            print('Failed,',headerTotalSpentlabel,'label is incorrect') 
        if totalSpentUsdLabel == 'USD':
           print('Passed,',totalSpentUsdLabel,'label is correct')
        else:
            print('Failed,',totalSpentUsdLabel,'label is incorrect')
        if headerStatuslabel == 'Status':
            print('Passed,',headerStatuslabel,'label is correct')
        else:
            print('Failed,',headerStatuslabel,'label is incorrect')
        if headerstatusvalue == 'Paused':
            print('Passed,',headerstatusvalue,'label is correct')
            print('Default status value is:',headerstatusvalue)
        else:
            print('Failed,',headerstatusvalue,'label is incorrect')

    def AdGroupSetUp(self,Behavior,Category,LocationGroup,Brand):
        driver.execute_script("window.scrollTo(0, 0);")
        audienctInfoIcon="You can now select a Location Group for Location Audience targeting. This will target users who have been to the stores within the selected Location Group. Your Location Group will be available for selection below only if you have already built Location Audience for the Location Group. If you have not built Location Audience for a Location Group yet, visit Location Manager to do so."
        print('%'*50)
        print('AdGroup details')
        allH3tags= driver.find_elements(By.TAG_NAME, 'h3')
        print('Count of H3 tags inside the Ad Group creation:',len(allH3tags)-1)
        for h3 in allH3tags:
            print(h3.text)
        nameYourAdGrouptag= driver.find_element(By.XPATH, "//h3[contains(text(),'Name your Ad Group')]").text
        selectAudiencestag = driver.find_element(By.XPATH, "//h3[contains(text(), 'Select audiences')]").text
        ApplyadditionalLocationFilterstag= driver.find_element(By.XPATH, "//h3[contains(text(),'additional location filters')]").text
        DriveToDestinationtag=driver.find_element(By.XPATH, "//h3[contains(text(),'Drive-To destination')]").text
        demogrphicstag=driver.find_element(By.XPATH, "//h3[contains(text(),'Demographics')]").text
        deviceTargetingtag=driver.find_element(By.XPATH, "//h3[contains(text(),'Device Targeting')]").text
        OptimizationStrategytag= driver.find_element(By.XPATH,"//h3[contains(text(),'Optimization Strategy')]").text
        publisherCategoryTag=driver.find_element(By.XPATH, "//h3[contains(text(),'Publisher Categories')]").text
        remessagingtag=driver.find_element(By.XPATH,"//h3[contains(text(),'remessaging')]").text
        
        if nameYourAdGrouptag == 'Name your Ad Group':
            print('Passed',nameYourAdGrouptag, 'is correct')
            adgroupInput=driver.find_element(By.XPATH, "//input[@id='adgroup-name']") #get_attribute('ng-if') .get_property('ng-if')
            adgroupInput.clear()
            adgroupInput.send_keys('surender')
            print('adgroup Name:',adgroupInput.text)
        else:
            print('Failed',nameYourAdGrouptag, 'is incorrect')     
        if selectAudiencestag == 'Select audiences':
            actions=ActionChains(driver)
            infoIcon=driver.find_element(By.XPATH, "//body/ui-view[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/h3[1]/new-feature[1]/a[1]/span[1]") #.//h3[contains(text(), 'Select audiences')]/*
            actions.move_to_element(infoIcon).perform()
            sleep(2)
            if infoIcon.get_attribute('uib-popover')==audienctInfoIcon:
                print("Passed, Audience tooltip is correct")
            else:
                print("Failed, Audience tooltip is incorrect")
            print('Passed',selectAudiencestag, 'is correct')
            audienceInputBox=driver.find_element(By.XPATH, "//input[@placeholder='Select a brand, category, behavioral, custom or location group audience']")
            # -------Behavior-------------------
            audienceInputBox.click()
            audienceInputBox.clear()
            audienceInputBox.send_keys(Behavior)
            sleep(1)
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Behavior')]"))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[(contains(text(),'"+Behavior+"'))]"))).click()
            # -------Category(Potato Growers)-------------------
            audienceInputBox.click()
            audienceInputBox.clear()
            audienceInputBox.send_keys(Category)
            sleep(1) 
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Category')]"))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[(contains(text(),'"+Category+"'))]"))).click()
            # -------Location Group(Live Nation)-------------------
            audienceInputBox.click()
            audienceInputBox.clear()
            audienceInputBox.send_keys(LocationGroup) 
            sleep(1)
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Location Group')]"))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[(contains(text(),'"+LocationGroup+"'))]"))).click()
            # -------Brand-------------------
            audienceInputBox.click()
            audienceInputBox.clear()
            audienceInputBox.send_keys(Brand) 
            sleep(1)
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Brand')]"))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[(contains(text(),'"+Brand+"'))]"))).click()
        else:
            print('Failed',selectAudiencestag, 'is incorrect')
        if ApplyadditionalLocationFilterstag == 'Apply additional location filters':
            print('Passed',ApplyadditionalLocationFilterstag, 'is correct')
        else:
            print('Failed',ApplyadditionalLocationFilterstag, 'is incorrect')
        if DriveToDestinationtag == 'Specify your Drive-To destination for ad group measurement':
            print('Passed',DriveToDestinationtag, 'is correct')
        else:
            print('Failed',DriveToDestinationtag, 'is incorrect')
        if demogrphicstag == 'Demographics':
            print('Passed',demogrphicstag, 'is correct')
        else:
            print('Failed',demogrphicstag, 'is incorrect')
        if deviceTargetingtag == 'Device Targeting':
            print('Passed',deviceTargetingtag, 'is correct')
        else:
            print('Failed',deviceTargetingtag, 'is incorrect')
        if OptimizationStrategytag == 'Optimization Strategy':
            print('Passed',OptimizationStrategytag, 'is correct')
        else:
            print('Failed',OptimizationStrategytag, 'is incorrect')
        if publisherCategoryTag == 'Publisher Categories':
            print('Passed',publisherCategoryTag, 'is correct')
        else:
            print('Failed',publisherCategoryTag, 'is incorrect')
        if remessagingtag == 'Build custom audience for remessaging users who see your ad':
            print('Passed',remessagingtag, 'is correct')
        else:
            print('Failed',remessagingtag, 'is incorrect')
        

c=campaignSetUp()
c.NewCampaignButton()
c.NewCampaignModel('Regression-Automation-testing','Pet Services','campaign-budget','Save')# 'adgroup-budget','campaign-budget','×','Save'
c.TargettingHeader()
c.deviceType()
# c.LeftHandDetails()
# c.RightHandDetials()
# c.AdGroupHeader()
c.AdGroupSetUp('Millennials','Potato Growers','Live Nation',"Costco") #Behavior,Category,LocationGroup,Brand #"Wendy's" "7-Eleven"
sleep(20)
driver.close()
