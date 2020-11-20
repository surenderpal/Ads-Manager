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
import collections
import random

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
driver.get('https://ads-release-3-17-np.groundtruth.com/')

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
        sleep(5)
        newCampaignButton=WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-campDash-newCampaign']")))
        # newCampaignButton=driver.find_element(By.XPATH, "//button[@id='btn-campDash-newCampaign']")
        if newCampaignButton.tag_name == 'button':
            driver.find_element(By.XPATH, "//span[contains(text(),'New Campaign')]").click()
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
            # category = driver.find_element(By.XPATH, "//input[@placeholder='Search and select a category']")
            AdGroupBudgetLabel = driver.find_element(By.XPATH, "//div[@class='radio-wrapper']/label[@for='inp-createCampModal-budgetAdgLevel']").text
            CampaignBudgetLabel = driver.find_element(By.XPATH, "//div[@class='radio-wrapper']/label[@for='inp-createCampModal-budgetCampLevel']").text
            CampaignLabelName = driver.find_element(By.XPATH, "//div[@class='name-field']/label[@for='inp-createCampModal-campName']").get_attribute('innerHTML')
            # CategoryLabelName = driver.find_element(By.XPATH, "//label[contains(text(),'Category')]").get_attribute('innerHTML')
            infoInnerText=driver.find_element(By.XPATH, "//label[@class= 'budget-title']/span").get_attribute('uib-popover') #tool tip text
            info=driver.find_element(By.XPATH, "//label[@class='budget-title']/span")# info tool tip
            note = driver.find_element(By.XPATH, '//p').text #Note warning inside campaign budget
 
            if CampaignLabelName == 'Campaign Name':
                print('Passed, Campaign Name Label is correct!!')
                driver.find_element(By.ID, "inp-createCampModal-campName").send_keys(CampaignName) #campaign name 
                # if CategoryLabelName == 'Category':
                #     print('Passed, Category Name Label is correct!!')
                #     if category.get_attribute('placeholder') == 'Search and select a category':
                #         print('Passed!!,Placeholder inside Category')
                #         category.click()
                #         sleep(2)
                #         category_li = driver.find_elements(By.XPATH, "//div[@class='gt-autocomplete-dropdown ng-scope']/ul/li")
                #         print('#' * 30)
                #         print('Count of category:',len(category_li))                        
                #         print('categories are listed below:-')
                #         for li in category_li:
                #             print(li.text)
                #         print('#' * 30)
                #         driver.find_element(By.XPATH,"//li[contains(text(),'"+categoryName+"')]").send_keys(categoryName)# category name:- Potato Growers
                #     else:
                #         print('Failed!!,Placeholder inside Category')
                # else:
                #     print('Failed, Category Name lable is Incorrect') 
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

    def AdGroupSetUp(self):
        driver.execute_script("window.scrollTo(0, 0);")
        print('%'*50)
        print('AdGroup details')
        allH3tags= driver.find_elements(By.TAG_NAME, 'h3')
        print('Count of H3 tags inside the Ad Group creation:',len(allH3tags)-1)
        for h3 in allH3tags:
            print(h3.text)
        nameYourAdGrouptag= driver.find_element(By.XPATH, "//h3[contains(text(),'Name your Ad Group')]")
        if nameYourAdGrouptag.text == 'Name your Ad Group':
            print('Passed',nameYourAdGrouptag, 'is correct')
            adgroupInput=driver.find_element(By.XPATH, "//input[@id='adgroup-name']") #get_attribute('ng-if') .get_property('ng-if')
            adgroupInput.clear()
            adgroupInput.send_keys('surender')
            print('adgroup Name:',adgroupInput.text)
        else:
            print('Failed',nameYourAdGrouptag, 'is incorrect')
    def selectAudience(self,Behavior,Category,LocationGroup,Brand,ExBehavior,ExCategory,ExBrand,ExLocationGroup):  
        audienctInfoIcon="You can now select a Location Group for Location Audience targeting. This will target users who have been to the stores within the selected Location Group. Your Location Group will be available for selection below only if you have already built Location Audience for the Location Group. If you have not built Location Audience for a Location Group yet, visit Location Manager to do so."
        lookalikesLabelTooltipText='Lookalikes increase scale of your brand-based location audience by adding users similar to the original audience set. Achieve scale increase (upto 10x of the original set) without significant impact on visitation performance. Click here to learn more.'
        selectAudiencestag = driver.find_element(By.XPATH, "//h3[contains(text(), 'Select audiences')]")
        if selectAudiencestag.text == 'Select audiences':
            actions=ActionChains(driver)
            infoIcon=driver.find_element(By.XPATH, "//body/ui-view[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/h3[1]/new-feature[1]/a[1]/span[1]") 
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
            sleep(2)
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Behavior')]"))).click()
            sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[(contains(text(),'"+Behavior+"'))]"))).click()
            # -------Category(Potato Growers)-------------------
            audienceInputBox.click()
            audienceInputBox.clear()
            audienceInputBox.send_keys(Category)
            sleep(2) 
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Category')]"))).click()
            sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[(contains(text(),'"+Category+"'))]"))).click()
            # -------Location Group(Live Nation)-------------------
            audienceInputBox.click()
            audienceInputBox.clear()
            audienceInputBox.send_keys(LocationGroup) 
            sleep(2)
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Location Group')]"))).click()
            sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[(contains(text(),'"+LocationGroup+"'))]"))).click()
            # -------Brand-------------------
            audienceInputBox.click()
            audienceInputBox.clear()
            audienceInputBox.send_keys(Brand) 
            sleep(4)
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Brand')]"))).click()
            sleep(2)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tab-pane ng-scope active']/li[(contains(text(),'"+Brand+"'))]"))).click()
            # -------lookalikes
            lookalikesInputBox=driver.find_element(By.ID,"inp-adGroupTargetingAud-lookalikeAudScale")
            lookalikesLabel = driver.find_element(By.XPATH, "//div[@class='lookalike']//label")
            lookalikesInfo = driver.find_element(By.XPATH, ".//div[@class='lookalike']//span")
            if lookalikesInputBox.is_selected() == True:
                print('By Default lookalikes Input box is checked')
                if lookalikesLabel.text == 'Include lookalikes to increase scale':
                    print('Passed, lookalikes label is correct')
                    actions=ActionChains(driver)
                    actions.move_to_element(lookalikesInfo).perform()
                    if lookalikesInfo.get_attribute('uib-popover') == lookalikesLabelTooltipText:
                        print('Passed,Lookalikes Info tooltip text is correct')
                    else:
                        print('Lookalikes Info tooltip text is incorrect')
                else:
                    print('Failed, lookalikes label is Incorrect')
            else:
                print('By Default lookalikes Input box is Unchecked')
        else:
            print('Failed',selectAudiencestag, 'is incorrect')
        # clicking on the lookalike checkbox
        driver.find_element(By.ID,"inp-adGroupTargetingAud-lookalikeAudScale").click()
        # 2x of original audience
        select=Select(driver.find_element(By.ID,'inp-adGroupTargetingAud-selectedLookalikeAud'))
        select.select_by_visible_text('4x of original audience')
        print('count of options, inside th lookalike dropdown:',len(select.options))
        print('options are listed below:')
        for option in select.options:
            print(option.text)
        # ---Exclude Audience---------
        element=driver.find_element(By.XPATH, "//a[contains(text(),'Exclude Audiences')]")
        driver.execute_script("arguments[0].scrollIntoView();", lookalikesLabel) 
        element.click()
        sleep(2)
        if driver.find_element(By.XPATH, "//h4[contains(text(),'Excluding Audience')]").text == 'Excluding Audience':
            print('Passed, Excluding Audience, heading!!')
            excludeInput = driver.find_element(By.XPATH, "//div[@class='exclude-fields']//input")
            if excludeInput.get_attribute('placeholder')=='Select a brand, category, behavioral, custom or location group audience':
                print('Passed, placeholder inside the exclude Audience input box is correct')
            else:
                print('Failed, placeholder inside the exclude Audience input box is incorrect')
        else:
            print('Failed, Excluding Audience, heading') 
        # click on exlude element
        excludeInputBox=driver.find_element(By.XPATH,"//section[1]/div/gt-autocomplete//input")
        excludeInputBox.click()
        excludeTabs=driver.find_elements(By.XPATH, "//a[@ng-click='select($event)']")
        print('Count of tabs inside the Exclude input box:',len(excludeTabs))
        for tab in excludeTabs:
            print(tab.text)
        excludeInputBox.clear()
        #----Behaviour----------
        excludeInputBox.send_keys(ExBehavior)
        sleep(2)        
        driver.find_element(By.XPATH, "//a[contains(text(),'Behavior')]").click() 
        sleep(1)
        driver.find_element(By.XPATH, "//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(),'"+ExBehavior+"')]").click()
        #----Category----------
        excludeInputBox.send_keys(ExCategory) 
        sleep(2)        
        driver.find_element(By.XPATH, "//a[contains(text(),'Category')]").click() 
        sleep(1)
        driver.find_element(By.XPATH, "//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(),'"+ExCategory+"')]").click()
        #----Brand----------
        excludeInputBox.send_keys(ExBrand)
        sleep(2)        
        driver.find_element(By.XPATH, "//a[contains(text(),'Brand')]").click() 
        sleep(1)
        driver.find_element(By.XPATH, "//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(),'"+ExBrand+"')]").click()
        #----Location Group----------
        excludeInputBox.send_keys(ExLocationGroup)
        sleep(2)       
        driver.find_element(By.XPATH, "//a[contains(text(),'Location Group')]").click() 
        sleep(1)
        driver.find_element(By.XPATH, "//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(),'"+ExLocationGroup+"')]").click()
        #scroll to the top of the page
        actions=ActionChains(driver)
        actions.move_to_element(selectAudiencestag).perform()
        # driver.execute_script("arguments[0].scrollIntoView();", nameYourAdGrouptag) 
        lilnksInSelectAudienceSetting=driver.find_elements(By.XPATH, "//div[@class='hyperlink-holder ng-scope']/a")
        print('count of links near the select audience setting:',len(lilnksInSelectAudienceSetting))
        for link in lilnksInSelectAudienceSetting:
            print(link.text)
            print(link.get_attribute('href'))
        locationGroupLinkInSelectAduience= driver.find_element(By.XPATH,"//div[@class='hyperlink-holder ng-scope']/a[contains(text(),'Add')]")
        if locationGroupLinkInSelectAduience.text == 'Add new location group':
            print('Passed, Link text passed')
        else:
            print('Failed, Link text failed')
        adsHandle=driver.current_window_handle
        driver.find_element(By.XPATH,"//div[@class='hyperlink-holder ng-scope']/a[contains(text(),'Add')]").click()
        handles=driver.window_handles
        for handle in handles:
            if handle!=adsHandle:
                driver.switch_to.window(handle)
                print('title of second window:',driver.title) #performed task on second window
                sleep(3)
                driver.close()
            driver.switch_to.window(adsHandle)
            print(driver.title)
#-------------Apply additional location filters---------------- 
    def additionalLocationFilter(self):#city,state,DMA,path
        driver.find_element(By.XPATH,"//li[contains(text(),'Location Filter')]").click()
        # driver.find_element(By.XPATH,"//li[contains(text(),'Location Filter')]").click()
        sleep(2)
        addLocFilterPlaceholder='Search and select city, state, DMA, zipcode, coordinates, or address'
        ApplyadditionalLocationFilterstag= driver.find_element(By.XPATH, "//h3[contains(text(),'additional location filters')]")
        if ApplyadditionalLocationFilterstag.text == 'Apply additional location filters':
            print('Passed',ApplyadditionalLocationFilterstag.text, 'is correct')
            addLocFilter=driver.find_element(By.XPATH, "//section[@id='location-filter']//input")
            addLocFilter.click()
            addLocFilter.clear()  
            if addLocFilter.get_attribute('placeholder') == addLocFilterPlaceholder:
                print('Passed, placeholder inside the additional location filter is correct')
                #tabs inside input box
                tabs=driver.find_elements(By.XPATH, "//li/a[@ng-click='select($event)']")
                print('count of tabs inside the additional location filter:',len(tabs))
                for tab in tabs:
                    print(tab.text)
        #---------city---------- 
                #key sending in input box
                addLocFilter.send_keys('Parkman, ME')
                sleep(2)
                driver.find_element(By.XPATH,"//a[contains(text(),'City')]").click()
                sleep(1)
                driver.find_element(By.XPATH,"//div[@class='tab-pane ng-scope active']/li[contains(text(), 'Parkman, ME')]").click()
        #---------state---------- 
                #key sending in input box
                addLocFilter.send_keys('Missouri')
                sleep(2)
                driver.find_element(By.XPATH,"//a[contains(text(),'State')]").click()
                sleep(1)
                driver.find_element(By.XPATH,"//div[@class='tab-pane ng-scope active']/li[contains(text(), 'Missouri')]").click()        
        #---------DMA---------- 
                #key sending in input box
                addLocFilter.send_keys('Austin, TX')
                sleep(2)
                driver.find_element(By.XPATH,"//a[contains(text(),'DMA')]").click()
                sleep(1)
                driver.find_element(By.XPATH,"//div[@class='tab-pane ng-scope active']/li[contains(text(), 'Austin, TX')]").click() 
            else:
                print('Failed, placeholder inside the additional location filter is incorrect')
        else:
            print('Failed',ApplyadditionalLocationFilterstag.text, 'is incorrect')
        geocoder=driver.find_element(By.LINK_TEXT,"Bulk location upload")
        if geocoder.text == 'Bulk location upload':
            print('Passed, Geocoder link text is correct')
            geocoder.click()
            geocoderUploaderText=driver.find_element(By.ID,"btn-superformModal-uploadFile")
            geocoderModelTitle=driver.find_element(By.XPATH,"//div[contains(text(),'Upload Location Filters')]")
            geocoerOrText=driver.find_element(By.XPATH,"//span[@class='or']")
            geocoderTemplateDownload=driver.find_element(By.LINK_TEXT,"Download template here")
            gecoderAppendCheckBox=driver.find_element(By.ID,"inp-superformModal-appendData")
            gecoderAppendText=driver.find_element(By.XPATH,"//label[@for='inp-superformModal-appendData']")
            sleep(2)
            if geocoderModelTitle.text == 'Upload Location Filters':
                print('Passed, Geocoder title is correct')
                if geocoderUploaderText.text=='Select from computer':
                    print('Passed, Geocder uploader text is correct')
                else:
                    print('text is:',geocoderUploaderText.text)
                    print('Failed, Geocoder uploader text is incorrect')
                if geocoerOrText.text=='OR':
                    print('Passed, "Or" text between the upload Location filter is correct')
                else:
                    print('Failed, "Or" text between the upload Location filter is incorrect')
                if geocoderTemplateDownload.text == 'Download template here':
                    print('Passed, template download text is correct')
                    # geocoderTemplateDownload.click()
                else:
                    print('Failed, template download text is incorrect')
                if gecoderAppendText.text == 'Append to existing location filters':
                    print('Passed, append text is correct')
                else:
                    print('Failed, append text is incorrect')
                if gecoderAppendCheckBox.is_selected() == False:
                    print('Passed, By default append checkbox is unchecked')
                    gecoderAppendCheckBox.click()
                    sleep(2)
                else:
                    print('By default append checkbox is checked')
                driver.find_element(By.XPATH,"//div[@id='btn-superformModal-uploadFile']/input").send_keys('/Users/surenderpal/Downloads/Creatives/Geocoders file/sample_geotarget.xlsx')
                sleep(5)
                geocoderSuccessUploadMessage=driver.find_element(By.XPATH,"//h3[@class='ng-binding']") #//h3[contains(text(),'rows were processed successfully.')]
                if geocoderSuccessUploadMessage.text=='All spreadsheet rows were processed successfully.':
                    print('Passed, spreadsheet successfull message is correct')
                else:
                    print('Failed, spreadsheet successfull message is incorrect')
                geocoderButtons=driver.find_elements(By.XPATH,"//div[@class='cta']/button")
                print('Count of buttons in Geocoder model:',len(geocoderButtons))
                for button in geocoderButtons:
                    print(button.text)       
                geoCoderCancelButton=driver.find_element(By.XPATH,"//button[contains(text(),'Cancel')]")                     
                if geoCoderCancelButton.text =='Cancel':
                    print('Passed, Cancel button text is correct')
                else:
                    print('Failed, Cancel button text is incorrect')
                geoCoderSaveButton=driver.find_element(By.XPATH,"//div[@class='cta']/button/span")
                if geoCoderSaveButton.text == 'Save':
                    print('Passed, save button text is correct')
                    geoCoderSaveButton.click()
                else:
                    print('Failed, save button text is correct')
            else:
                print('Failed, Geocder title is incorrect')
        else:
            print('Failed, Geocoder link text is incorrect')
        #-----drive to destination-----------
    def DriveToDestinationt(self):
        DriveToDestinationtag=driver.find_element(By.XPATH, "//h3[contains(text(),'Drive-To destination')]")
        element=driver.find_element(By.XPATH,"//h3[contains(text(),'Drive-To destination')]")
        driver.execute_script("arguments[0].scrollIntoView();",element)
        if DriveToDestinationtag.text == 'Specify your Drive-To destination for ad group measurement':
            print('Passed',DriveToDestinationtag.text, 'is correct')
            dTDLables=driver.find_elements(By.XPATH,"//div[@class='measurement-options']//label")
            print('count of labels in drive to destination:',len(dTDLables))
            print('Labels that are available under the Drive to destination are listed below:-')
            for label in dTDLables:
                print(label.text)
            dTDRadioBtn=driver.find_elements(By.XPATH,"//div[@class='measurement-options']//input")
            print('Count of checkbox present inside the drive to destination:',len(dTDRadioBtn))
            if driver.find_element(By.ID,"inp-adgTargetSup-measurementNational").get_attribute('type') == 'radio':
                print('Passed,input box present under drive to destination is Radio button')
                if driver.find_element(By.ID,"inp-adgTargetSup-measurementNational").is_selected() == True:
                    print('Default selected radio button is:No Drive-To location, conversion will occur online')
                else:
                    print('Default selected radio button is incorrect')
                button=driver.find_element(By.ID,"inp-adgTargetSup-measurementList")
                driver.execute_script("arguments[0].click();", button)
                sleep(2)
                # dTDsublabels=driver.find_elements(By.XPATH,"//div[@class='ng-scope']/label")
                # print('count of labels appeared after click on Drive to location radio button:',len(dTDsublabels))
                # for label in dTDsublabels:
                #     print(label.text)
                # dTDCheckBox=driver.find_elements(By.XPATH,"//div[@class='ng-scope']/input")
                # print('count of checkboxs appeared after click on Drive to location radio button:',len(dTDCheckBox))
            else:
                print('Failed,input box present under drive to destination is not Radio button')
            # storeVisitation=driver.find_element(By.ID,"inp-adgTargetSup-enableStoreVisitation")
            # if storeVisitation.is_displayed() == True and storeVisitation.is_enabled == False:
            #     storeVisitationLabel=driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-enableStoreVisitation']")
            #     if storeVisitationLabel.text == 'Enable Store Visitation':
            #         print('Passed, Enable Store Visitation text is correct')
            #     else:
            #         print('Failed, Enable Store Visitation text is incorrect')
            #     visitationLiftLabel=driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-enableStoreVisitationLift']")
            #     if visitationLiftLabel.text == 'Enable Store Visitation Lift':
            #         print('Passed, Enable Store Visitation Lift text is correct') 
            #     else:
            #         print('Failed, Enable Store Visitation Lift text is incorrect')
            #     # in stock targetting code
            #     print('Passed, By default Enable Store Visitation is disabled')
            # else:
            #     print('False, By default Enable Store Visitation is not disabled')
        else:
            print('Failed',DriveToDestinationtag.text, 'is incorrect')
        # working with input box (list drop-down)
        dTDInputBox=driver.find_element(By.XPATH,"//input[contains(@placeholder, 'custom location group')]")
        dTDInputBox.click()
        if dTDInputBox.get_attribute('placeholder') == 'Search and select a GroundTruth brand or your custom location group':
            print('Passed, placeholder inside the drive to destination is correct')
            tabsCountDTD=driver.find_elements(By.XPATH,"//a[@ng-click='select($event)']")
            print('Count of tabs inside Drive to destination input box',len(tabsCountDTD))
            for tab in tabsCountDTD:
                print(tab.text)
            dTDInputBox.send_keys('KFC')
            driver.find_element(By.XPATH,"//a[contains(text(),'Brand')]").click()
            driver.find_element(By.XPATH,"//li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(), 'KFC')]").click()
            dTDInputBox.clear()
            dTDInputBox.send_keys('Lexus')
            driver.find_element(By.XPATH,"//a[contains(text(),'Location Group')]").click()
            driver.find_element(By.XPATH,"//div[@class='tab-pane ng-scope active']/li[@class='autocomplete-item ng-binding ng-scope highlighted' and contains(text(), 'Lexus')]").click()
            dTDInputBox.clear()
            dTDSelectedOptions=driver.find_elements(By.XPATH,"//section[@id='measurements']//ul/li")
            print('count of selected options are:',len(dTDSelectedOptions))
            for option in dTDSelectedOptions:
                print('selected option is :',option.text)
        else:
            print('Failed, placeholder inside the drive to destination is correct')
# ---------demographics section----------
    def Demographics(self):
        demogrphicstag=driver.find_element(By.XPATH, "//h3[contains(text(),'Demographics')]")
        if demogrphicstag.text == 'Demographics':
            print('Passed',demogrphicstag.text, ' headind is correct')
            element=driver.find_element(By.XPATH,"//li[contains(text(),'Drive-To Locations')]")
            element.click()
            demoCheckbox=driver.find_element(By.XPATH,"//input[@id='inp-adgTargetSup-selectAllDemographics' and @type='checkbox']")
            demoLabel=driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-selectAllDemographics']")
            if demoLabel.text=='Show your ads to all demographics':
                print('Passed',demoLabel.text,'is correct')
            else:
                print('Failed',demoLabel.text,'is incorrect')
            demoCheckbox=driver.find_element(By.ID,"inp-adgTargetSup-selectAllDemographics") 
            if demoCheckbox.get_attribute('type') == 'checkbox':
                if demoCheckbox.is_selected() == True:
                    driver.execute_script("arguments[0].click();", demoCheckbox) 
                    print('Passed,By default Demographics is checked and input type is checkbox')
                else:
                    print('Failed,By default Demographics is unchecked and input type is no checkbox')
            else:
                print('Failed, input type is not checkbox')
        else:
            print('Failed',demogrphicstag.text, 'is incorrect')
        demoLabels=driver.find_elements(By.XPATH,"//section[@id='demographics']//span[@class='input-container-label']")
        print('Count of labels available after Unchecking on the demographics checkbox',len(demoLabels))
        for label in demoLabels:
            print(label.text)
        countDemoCheck=driver.find_elements(By.XPATH,"//section[@id='demographics']//input[contains(@id,'inp-adgTargetSup')]")
        print('Count of checkboxs available under the Demograpics section:',(len(countDemoCheck)-1))
        checkedCheckbox=driver.find_elements(By.XPATH,"//section[@id='demographics']//input[@class='ng-pristine ng-untouched ng-valid ng-not-empty']")
        print('Count of checkbox, that are checked by default:',len(checkedCheckbox))
        UncheckedCheckboxLabel=driver.find_elements(By.XPATH,"//section[@id='demographics']//input[@class='ng-pristine ng-untouched ng-valid ng-empty']/../label")
        print('count of Unchecked checkbox available are:',len(UncheckedCheckboxLabel))
        demoActualListChecked=['All', 'All', 'All', 'All']
        demoExpectedListChecked=[]
        for checked in checkedCheckbox:
            print('Input type is:',checked.get_attribute('type'))
            demoExpectedListChecked.append(driver.find_element(By.XPATH,"//section[@id='demographics']//input[@class='ng-pristine ng-untouched ng-valid ng-not-empty']/../label").text)
        if collections.Counter(demoExpectedListChecked) == collections.Counter(demoActualListChecked):
            print('Passed, By default Checked checkbox are correct')
        else:
            print('Failed, By default Checked checkbox is incorrect') 
        genderLabel=driver.find_element(By.XPATH,"//span[contains(text(),'Gender')]")
        houseHoldLabel=driver.find_element(By.XPATH,"//span[contains(text(),'Household')]")
        ethnicityLabel=driver.find_element(By.XPATH,"//span[contains(text(),'Ethnicity')]")
        AgeLabel=driver.find_element(By.XPATH,"//span[contains(text(),'AGE GROUPS')]")
        drinkingLabel=driver.find_element(By.XPATH,"//span[contains(text(),'Drinking')]")

        if genderLabel.text == 'GENDER':
            print('Passed,',genderLabel.text,'label is correct')
        else:
            print('Failed,',genderLabel.text,'label is incorrect')
        if houseHoldLabel.text == 'HOUSEHOLD INCOME ($)':
            print('Passed,',houseHoldLabel.text,'label is correct')
        else:
            print('Failed,',houseHoldLabel.text,'label is incorrect')
        if ethnicityLabel.text == 'ETHNICITY':
            print('Passed,',ethnicityLabel.text,'label is correct')
            ageInfo=driver.find_element(By.XPATH,"//span[contains(text(),'AGE')]/span")
            actions=ActionChains(driver)
            actions.move_to_element(ageInfo).perform()
            sleep(2)
            if ageInfo.get_attribute('uib-popover')=='Age range 13-17 is no longer available for targeting.':
                print('Passed, tooltip text inside the Age Group is correct')
            else:
                print('Failed, tooltip text inside the Age Group is incorrect')
        else:
            print('Failed,',ethnicityLabel.text,'label is incorrect')
        if driver.find_element(By.XPATH,"//span[@id='age-groups']").text == 'AGE GROUPS':
            print(driver.find_element(By.XPATH,"//span[@id='age-groups']").text)
        else:
            print('Failed,',AgeLabel.text,'label is incorrect')
            print(driver.find_element(By.XPATH,"//span[@id='age-groups']").text)
        if drinkingLabel.text == 'TARGET USERS OVER LEGAL DRINKING AGE':
            print('Passed,',drinkingLabel.text,'label is correct')
        else:
            print('Failed,',drinkingLabel.text,'label is incorrect')
        demoActualListUnchecked=['Male', 'Female', '0-50K', '50-100K', '100-150K', '150-200K', '200K+', 'Asian', 'African American', 'Hispanic or Latino', '18-24', '25-34', '35-44', '45-54', '55-64', '65+', 'Alcohol Age']
        l=[]
        for label in UncheckedCheckboxLabel:
            l.append(label.text)
        # comparing actual vs expected list to verify the content of list
        if collections.Counter(demoActualListUnchecked) == collections.Counter(l):
            print('Passed, By default unchecked checkbox are correct')
        else:
            print('Failed, By defaylt unchecked checkbox is incorrect') 

#---device targetting function start here-----
    def deviceTargeting(self):
        print('-'*50)
        driver.find_element(By.XPATH,"//li[contains(text(),'Demographics')]").click()
        sleep(2)
        deviceTargetingtag=driver.find_element(By.XPATH, "//h3[contains(text(),'Device Targeting')]")
        deviceSubLabel=driver.find_element(By.XPATH,"//label[contains(text(),'default device types')]")
        # click on Device Targetting checkbox
        # Checkbox=driver.find_element(By.ID,'inp-adgTargetSup-toggleAllTechnographics') #deive targetting checkbox, 
        # driver.execute_script("arguments[0].click();",Checkbox) #unchecked it
        if deviceTargetingtag.text == 'Device Targeting':
            print('Passed',deviceTargetingtag.text, 'is correct')
            #check sub label "Show your ads to default device types"
            if deviceSubLabel.text=='Show your ads to default device types':
                print('Passed,',deviceSubLabel.text,' label is correct')
            else:
                print('Failed,',deviceSubLabel.text,' label is incorrect')
        else:
            print('Failed',deviceTargetingtag.text, 'is incorrect')
        
        # all rows labels
        targetingFieldLabel=driver.find_elements(By.XPATH,"//section[@id='technographics']//span['input-container-label']") #labels like enviro, mobile os, mobile carrier
        ActualTargetingFieldLabelList=['ENVIRONMENT','MOBILE OPERATING SYSTEM','MOBILE CARRIER']
        ExpectedTargetingFieldLabelList=[]
        print('Count of labels are:',len(targetingFieldLabel))
        for label in targetingFieldLabel:
            ExpectedTargetingFieldLabelList.append(label.text)
        if collections.Counter(ActualTargetingFieldLabelList) == collections.Counter(ExpectedTargetingFieldLabelList):
            print('Passed, By default Targeting Field Labels are correct',ActualTargetingFieldLabelList)
        else:
            print('Drive To Destinationt labels are incorrect',ExpectedTargetingFieldLabelList)

        # clicking on the Mobile carrier checkbox

        driver.find_element(By.ID,"inp-adgTargetSup-toggleAllCarriers").click()
        sleep(2)
        # testing all checkbox Device Targetting
        DeviceTargettingCheckboxLabel=driver.find_elements(By.XPATH,"//section[@id='technographics']//input/../label")
        print('Count of labels present inside the Device Targetting:',len(DeviceTargettingCheckboxLabel))
        ActualDeviceTargettingCheckboxLabelList=['Show your ads to default device types', 'ALL', 'MOBILE APP', 'MOBILE WEB', 'ALL', 'iOS', 'ANDROID', 'OTHERS', 'ALL', 'Alltel', 'Appalachian Wireless', 'AT&T', 'Bluegrass Cellular', 'Cincinnati Bell', 'Corr Wireless', 'Cricket', 'Metro PCS', 'Plateau Wireless', 'SIMMETRY', 'Sprint', 'T-Mobile', 'US Cellular', 'Verizon Wireless', 'WiFi']
        ExpectedDeviceTargettingCheckboxLabelList=[]
        for label in DeviceTargettingCheckboxLabel:
            ExpectedDeviceTargettingCheckboxLabelList.append(label.text)
        if collections.Counter(ActualDeviceTargettingCheckboxLabelList) == collections.Counter(ExpectedDeviceTargettingCheckboxLabelList):
            print('Passed, all Device Targetting Labels are correct')
        else:
            print('Failed, all Device Targetting Labels are incorrect',ExpectedDeviceTargettingCheckboxLabelList)
        print('All checkboxs under the Device Targetting:',ExpectedDeviceTargettingCheckboxLabelList)

        # testing default unchecked checkbox Device Targetting

        defaultUncheckedCheckbox=driver.find_elements(By.XPATH,"//section[@id='technographics']//input[@class='ng-pristine ng-untouched ng-valid ng-empty' or @id='inp-adgTargetSup-osiOS' or @class='ng-pristine ng-valid ng-empty ng-touched']/../label")
        ActualUncheckedCheckboxList=['Show your ads to default device types', 'ALL', 'iOS', 'ANDROID', 'OTHERS']
        ExpectedUncheckedCheckboxList=[]
        print('Count of unchecked labels are:',len(defaultUncheckedCheckbox))
        for label in defaultUncheckedCheckbox:
            ExpectedUncheckedCheckboxList.append(label.text)
        if collections.Counter(ActualUncheckedCheckboxList) == collections.Counter(ExpectedUncheckedCheckboxList):
            print('Passed, all Device Targetting Labels are correct')
        else:
            print('Failed, all Device Targetting Labels are incorrect')
        print('Labels are Unchecked by default are:',ExpectedUncheckedCheckboxList)

        # testing checked checkbox Device Targetting

        ActualCheckedCheckboxList=['MOBILE APP', 'MOBILE WEB', 'ALL', 'Alltel', 'Appalachian Wireless', 'AT&T', 'Bluegrass Cellular', 'Cincinnati Bell', 'Corr Wireless', 'Cricket', 'Metro PCS', 'Plateau Wireless', 'SIMMETRY', 'Sprint', 'T-Mobile', 'US Cellular', 'Verizon Wireless', 'WiFi']
        ExpectedCheckedCheckboxList=[]
        defaultCheckedCheckboxLabels=driver.find_elements(By.XPATH,"//section[@id='technographics']//input[@class='ng-pristine ng-untouched ng-valid ng-not-empty']/../label")
        for label in defaultCheckedCheckboxLabels:
            ExpectedCheckedCheckboxList.append(label.text)
        print(ExpectedCheckedCheckboxList)
        if collections.Counter(ActualCheckedCheckboxList) == collections.Counter(ExpectedCheckedCheckboxList):
            print('Passed, all Device Targetting Checked Labels are correct',ActualCheckedCheckboxList)
        else:
            print('Failed, all Device Targetting Checked Labels are incorrect',ExpectedCheckedCheckboxList)



#---Optimization Strategy function starts here-----  
    def OptimizationStrategy(self):  
        print('#'*50)
        sleep(2) 
        driver.find_element(By.XPATH,"//li[contains(text(),'Optimization Strategy')]").click()  
        OptimizationStrategyHding= driver.find_element(By.XPATH,"//h3[contains(text(),'Optimization Strategy')]")
        if OptimizationStrategyHding.text == 'Optimization Strategy':
            print('Passed',OptimizationStrategyHding.text, 'Heading is correct')
        else:
            print('Failed',OptimizationStrategyHding.text, 'Heading is incorrect')
        OptStrRadioBtn=driver.find_elements(By.XPATH,"//section[@id='optimization-strategy']//input[@type='radio']")
        OptStrRadioBtnLbl=driver.find_elements(By.XPATH,"//div[@class='optimization-strategy-options']//input")
        print('Count of radio buttons under the Optimization Strategy are:',len(OptStrRadioBtn))
        radioBtnPara=driver.find_element(By.XPATH,"//div[@class='optimization-info ng-binding']")
        actualP=['Maximize delivery to get the most impressions.', 'We’ll deliver your ads to people that are expected to provide more click through to your landing page.', 'We’ll deliver your ads to people that are expected to provide more secondary action clicks on your landing page. This optimization requires you to use GroundTruth landing pages. The threshold is the number of secondary actions expected per 10,000 impressions.', 'We’ll deliver your ads to people that are expected to provide better conversions on your site. GroundTruth Tracking Pixels must be generated and used for this optimization to work (Tracking Pixels can be added on the Budget & Schedule section).']
        exptectedP=[]
        radioLbls=driver.find_element(By.XPATH,"//div[@class='optimization-strategy-options']//input/../label")
        actualRadioLbls=['Delivery', 'Delivery', 'Delivery', 'Delivery']
        expectedRadioLbls=[]

        # clicked on all radio buttons, tested radio labels and respective paragraphs 
        for btn in OptStrRadioBtnLbl:
            # btn.click()
            driver.execute_script("arguments[0].click();",btn)
            exptectedP.append(radioBtnPara.text)
            expectedRadioLbls.append(radioLbls.text)
            sleep(2)
        # tested radio button labels
        if collections.Counter(actualRadioLbls) == collections.Counter(expectedRadioLbls):
            print('Passed, radio button labels, under the',OptimizationStrategyHding.text,'is correct')
        else:
            print('Failed, radio button labels, under the',OptimizationStrategyHding.text,'is incorrect')
        print('Radio button labels are:',expectedRadioLbls)

        # tested radio button paragraph
        if collections.Counter(actualP) == collections.Counter(exptectedP):
            print('Passed, paragraphs under the',OptimizationStrategyHding.text,'is correct')
        else:
            print('Failed, paragraphs under the',OptimizationStrategyHding.text,'is incorrect')
        # print('Paragraphs under the',OptimizationStrategyHding.text,'is:',exptectedP) # uncomment working fine
        # Under click radio button 
        '''testing checkbox,label and rest of things'''


        # clicking on the Click radio button
        driver.execute_script("arguments[0].click();",driver.find_element(By.CSS_SELECTOR,"#inp-adgTargetSup-optimizationGoal0"))


        if driver.find_element(By.ID,'inp-adgTargetSup-optimizationAuto0').get_attribute('type') == 'checkbox':
            if driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationAuto0']").text == 'AUTO':
                autoChkBox=driver.find_element(By.CSS_SELECTOR,"#inp-adgTargetSup-optimizationAuto0")
                # perform before click test on label
                BeforeClickDefltCTRThrsholdLabel= driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationCtrThreshold']")
                if BeforeClickDefltCTRThrsholdLabel.text == 'DEFAULT CTR THRESHOLD':
                    print('Passed, before click',BeforeClickDefltCTRThrsholdLabel.text,'lable is correct')
                else:
                    print('Failed, before click',BeforeClickDefltCTRThrsholdLabel.text,'lable is incorrect')
                # clicking on the checkbox'AUTO'
                driver.execute_script("arguments[0].click();",autoChkBox)
                sleep(2)
                # Testing the value of 0.3
                if driver.find_element(By.NAME,"optimization_ctr_threshold").get_attribute('value')=='0.3':
                    print('Passed, default value inside the input box is correct and value is:',driver.find_element(By.NAME,"optimization_ctr_threshold").get_attribute('value'))
                else:
                    print('Failed, default value inside the input box is incorrect and value is:',driver.find_element(By.NAME,"optimization_ctr_threshold").get_attribute('value'))
                
                AfterClickDefltCTRThrsholdLabel=driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationCtrThreshold']")
                # testing 'DEFAULT CTR THRESHOLD' label under the click radio button
                if AfterClickDefltCTRThrsholdLabel.text == 'CTR THRESHOLD':
                    print('Passed,','After click on checkbox ',AfterClickDefltCTRThrsholdLabel.text,'lable under Click radio button is correct')
                else:
                    print('Failed,','After click on checkbox ',AfterClickDefltCTRThrsholdLabel.text,'lable under Click radio button is incorrect') #fail 
            else:
                print('Element label is incorrect')
        else:
            print('Element is not of checkbox type')


        # clicking on the SAR radio button
        driver.execute_script("arguments[0].click();",driver.find_element(By.CSS_SELECTOR,"#inp-adgTargetSup-optimizationGoal2"))
        if driver.find_element(By.ID,'inp-adgTargetSup-optimizationAuto1').get_attribute('type') == 'checkbox':
            if driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationAuto1']").text == 'AUTO':
                autoChkBox=driver.find_element(By.CSS_SELECTOR,"#inp-adgTargetSup-optimizationAuto1")
                # perform before click test on label
                BeforeClickDefltCTRThrsholdLabel= driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationSarThreshold']")
                if BeforeClickDefltCTRThrsholdLabel.text == 'DEFAULT SAR THRESHOLD PER 10000 IMPRESSIONS':
                    print('Passed, before click',BeforeClickDefltCTRThrsholdLabel.text,'lable is correct')
                else:
                    print('Failed, before click',BeforeClickDefltCTRThrsholdLabel.text,'lable is incorrect')
                # clicking on the checkbox'AUTO'
                driver.execute_script("arguments[0].click();",autoChkBox)
                sleep(2)
                # Testing the value of 0.3
                if driver.find_element(By.NAME,"optimization_sar_threshold").get_attribute('value')=='3':
                    print('Passed, default value inside the input box is correct and value is:',driver.find_element(By.NAME,"optimization_sar_threshold").get_attribute('value'))
                else:
                    print('Failed, default value inside the input box is incorrect and value is:',driver.find_element(By.NAME,"optimization_sar_threshold").get_attribute('value'))
                
                AfterClickDefltCTRThrsholdLabel=driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationSarThreshold']")
                # testing 'DEFAULT CTR THRESHOLD' label under the click radio button
                if AfterClickDefltCTRThrsholdLabel.text == 'SAR THRESHOLD PER 10000 IMPRESSIONS':
                    print('Passed,','After click on checkbox ',AfterClickDefltCTRThrsholdLabel.text,'lable under Click radio button is correct')
                else:
                    print('Failed,','After click on checkbox ',AfterClickDefltCTRThrsholdLabel.text,'lable under Click radio button is incorrect') #fail 
            else:
                print('Element label is incorrect')
        else:
            print('Element is not of checkbox type')

    # clicking on the Conversion radio button
        driver.execute_script("arguments[0].click();",driver.find_element(By.CSS_SELECTOR,"#inp-adgTargetSup-optimizationGoal3"))


        if driver.find_element(By.ID,'inp-adgTargetSup-optimizationAuto2').get_attribute('type') == 'checkbox':
            if driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationAuto2']").text == 'AUTO':
                autoChkBox=driver.find_element(By.CSS_SELECTOR,"#inp-adgTargetSup-optimizationAuto2")
                # perform before click test on label
                BeforeClickDefltConversionThrsholdLabel= driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationConversionThreshold']")
                if BeforeClickDefltConversionThrsholdLabel.text == 'DEFAULT CONVERSION THRESHOLD':
                    print('Passed, before click',BeforeClickDefltConversionThrsholdLabel.text,'lable is correct')
                else:
                    print('Failed, before click',BeforeClickDefltConversionThrsholdLabel.text,'lable is incorrect')
                # clicking on the checkbox'AUTO'
                driver.execute_script("arguments[0].click();",autoChkBox)
                sleep(2)
                # Testing the value of 0.3
                if driver.find_element(By.NAME,"optimization_conversion_threshold").get_attribute('value')=='0':
                    print('Passed, default value inside the input box is correct and value is:',driver.find_element(By.NAME,"optimization_conversion_threshold").get_attribute('value'))
                else:
                    print('Failed, default value inside the input box is incorrect and value is:',driver.find_element(By.NAME,"optimization_conversion_threshold").get_attribute('value'))
                
                AfterClickDefltConversionThrsholdLabel=driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationConversionThreshold']")
                # testing 'DEFAULT CTR THRESHOLD' label under the click radio button
                if AfterClickDefltConversionThrsholdLabel.text == 'CONVERSION THRESHOLD 0%':
                    print('Passed,','After click on checkbox ',AfterClickDefltConversionThrsholdLabel.text,'lable under Click radio button is correct')
                else:
                    print('Failed,','After click on checkbox ',AfterClickDefltConversionThrsholdLabel.text,'lable under Click radio button is incorrect') #fail 
            else:
                print('Element label is incorrect')
        else:
            print('Element is not of checkbox type')
        # testing disabled checkbox, label and default value
        disabledChkBox=driver.find_element(By.ID,"inp-adgTargetSup-optimizationAuto0")
        
        if disabledChkBox.get_attribute('type') == 'checkbox':
            print('Disabled element is of type checkbox')
            # check wether element is disabled or not

            # check label
            disabledLabel=driver.find_element(By.XPATH,"//label[@for='inp-adgTargetSup-optimizationCtrThreshold']")
            if disabledLabel.text == 'CTR THRESHOLD 0.3%':
                print('Passed,Label is correct',disabledLabel.text)
            else:
                print('Failed,Label is incorrect',disabledLabel.text)
            # Testing the value of 0.3
            if driver.find_element(By.NAME,"optimization_ctr_threshold").get_attribute('value')=='0.3':
                print('Passed, default value inside the input box is correct and value is:',driver.find_element(By.NAME,"optimization_ctr_threshold").get_attribute('value'))
            else:
                print('Failed, default value inside the input box is incorrect and value is:',driver.find_element(By.NAME,"optimization_ctr_threshold").get_attribute('value'))
        else:
            print('Disabled element is of type checkbox')


#---Publisher Category function starts here-----
    def publisherCategory(self):
        print('*'*50)
        driver.find_element(By.XPATH,"//li[contains(text(),'Publisher Categories')]").click()
        publisherCategoryTag=driver.find_element(By.XPATH, "//h3[contains(text(),'Publisher Categories')]")
        if publisherCategoryTag.text == 'Publisher Categories':
            print('Passed',publisherCategoryTag.text, 'is correct')
        else:
            print('Failed',publisherCategoryTag.text, 'is incorrect')
        # testing category label
        allCategories=driver.find_element(By.XPATH,"//label[contains(text(),'All Categories')]")
        if allCategories.text == 'All Categories':
            print('Passed,',allCategories.text,'label is correct')
        else:
            print('Failed,',allCategories.text,'label is incorrect') 
        catLabel=driver.find_element(By.ID,'inp-adgTargetSup-selectAllPublisherCats')
        driver.execute_script("arguments[0].click();",catLabel)  
        # testing all checkbox inside the publisher category
        chkBoxes=driver.find_elements(By.XPATH,"//section[@id='publisher-categories']//input")
        # code to check all input boxes are selected
        actualPubCatChkLbl=['deselected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected', 'selected']
        expectedPubCatChkLbl=[]
        for chkBox in chkBoxes:
            if chkBox.is_selected()==True:
                expectedPubCatChkLbl.append('selected')
            else:
                expectedPubCatChkLbl.append('deselected')
        if collections.Counter(actualPubCatChkLbl) == collections.Counter(expectedPubCatChkLbl):
            print('Passed, all labels are selected')
        else:
            print('Failed, all labels are unselected')
        print(expectedPubCatChkLbl)
        print('Count of checkboxes under Publisher Categories are:',len(chkBoxes))
        chkBoxesLbl=driver.find_elements(By.XPATH,"//section[@id='publisher-categories']//input/../label")
        AcutalchkBoxLbl=['Arts & Entertainment', 'Automotive', 'Books & Literature', 'Business', 'Careers', 'Comic Books', 'Education', 'Family & Parenting', 'Finance', 'Food & Drink', 'Hobbies & Interests', 'Home & Garden', "Law, Gov't & Politics", 'Lifestyle', 'Medical, Health & Fitness', 'Movies & Video', 'Music', 'Navigation', 'News', 'Non-Standard Content', 'Personalization', 'Pets', 'Photography', 'Productivity', 'Real Estate', 'Religion & Spirituality', 'Science', 'Shopping', 'Social', 'Society', 'Sports', 'Style & Fashion', 'Technology & Computing', 'Tools', 'Travel', 'Uncategorized', 'Video & Computer Games', 'Weather']
        ExpectedChkBoxLbl=[]
        for lbl in chkBoxesLbl:
            ExpectedChkBoxLbl.append(lbl.text)
        if collections.Counter(AcutalchkBoxLbl) == collections.Counter(ExpectedChkBoxLbl):
            print('Passed, all Device Targetting Checked Labels are correct')
        else:
            print('Failed, all Device Targetting Checked Labels are incorrect')
            print(ExpectedChkBoxLbl)
        

# ---custom audience function starts here-----
    def BuildCustomAudience(self):
        print('@'*50)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        remessagingtag=driver.find_element(By.XPATH,"//h3[contains(text(),'remessaging')]")
        if remessagingtag.text == 'Build custom audience for remessaging users who see your ad':
            print('Passed',remessagingtag.text, 'is correct')
            # driver.execute_script("arguments[0].scrollIntoView();",element)
        else:
            print('Failed',remessagingtag.text, 'is incorrect')
        # testing build audience label 
        buildAudienceLbl=driver.find_element(By.XPATH,"//section[@id='build-audience']//input/../label")
        if buildAudienceLbl.text == 'Build Audience':
            print('Passed,',buildAudienceLbl.text,' label is correct')
        else:
            print('Failed,',buildAudienceLbl.text,' label is incorrect')

        buildAudienceInput=driver.find_element(By.ID,'inp-adgTargetSup-buildAudience')
        buildAudienceInput.click()
        audName=driver.find_element(By.XPATH,"//span[contains(text(),'Audience Name')]")
        if audName.text == 'AUDIENCE NAME':
            print('Passed,',audName.text,'lable is correct')
        else:
            print('Failed,',audName.text,'lable is incorrect')
        input=driver.find_element(By.ID,"inp-adgTargetSup-audienceName")#.send_keys('testing-3.16')
        if input.tag_name == 'input':
            input.send_keys('testing-3.17-',random.randint(1,100000)) #add random no for uniqueness
        driver.find_element(By.ID,"btn-adgTargetSup-next").click() #next button clicked
        sleep(10)
class Createives():
    '''here we will set up creatives, copy, delete, edit, active, pause and other operations peform '''
    # # clicking on creative directly
    # driver.find_element(By.XPATH,"//div[contains(text(),'Ad Creatives')]").click()

    def CreativeDetailsVerify(self):
        print('+'*50)
        newCreativeBtn=WebDriverWait(driver,40).until((EC.element_to_be_clickable((By.ID,"btn-adgCreatives-newCreative"))))
        # newCreativeBtn=driver.find_element(By.ID,'btn-adgCreatives-newCreative')
        # testing button type and label and extracting label name
        if newCreativeBtn.tag_name == 'button' and newCreativeBtn.text == 'New Creative':
            print('Elemtent is of Button type and label text is:',newCreativeBtn.text) 
        else:
            print('Element is not of button type, it is of type:',newCreativeBtn.tag_name)
        addCreativeImage=WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='create-new-item-guide creative ng-scope']/img")))
        # Validating creative src
        if addCreativeImage.get_attribute("src") == 'https://cf.groundtruth.com/content/myfootprints/v1/img/assist_creative.png' and addCreativeImage.get_attribute('alt') == 'Create a new creative':
            print('Passed, Creative src is correct and it is:',addCreativeImage.get_attribute("src"))
            print('Passed, Creative alt text is correct and it is:',addCreativeImage.get_attribute('alt'))
            if addCreativeImage.is_displayed() == True:
                print('Passed, Creative image is displayed')
            else:
                print('Failed, Creative image is displayed')
        else:
            print('Failed, Creative src is incorrect',addCreativeImage.get_attribute("src"))
            print(addCreativeImage.get_attribute('alt'))
            print('image displayed:',addCreativeImage.is_displayed())

    def newCreativeDetails(self): #verify all form details
        creativeBtn=driver.find_element(By.XPATH,"//button[@id='btn-adgCreatives-newCreative']") #creative button
        creativeBtn.click() #clicking on the new creative button
        sleep(2)
        print('clicked on new creative')
        expectedTabs=[]
        actualTabs=['IMAGE', 'SCRIPT', 'VIDEO', 'HTML5']
        tabs=driver.find_elements(By.XPATH,"//div[@class='gt-tabs ng-isolate-scope']/ul/li/a")
        sleep(2)
        for tab in tabs:
            expectedTabs.append(tab.text)
            tab.click()
            print('clicked on tab:',tab.text)
            sleep(2)
        if collections.Counter(actualTabs) == collections.Counter(expectedTabs):
            print('Passed, all tabs links are correct')
        else:
            print('Failed, all tabs links are incorrect:',expectedTabs)
            sleep(2)
        # testing cancel button
        elementPos=driver.find_element(By.XPATH,"//div[@id='modalId']//ul//li/a[contains(text(),'Image')]")
        actions=ActionChains(driver)
        actions.move_to_element(elementPos).perform()
        cancel=WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//span[@ng-click='cancel()']")))
        cancel.click()

    def ImageCreative(self,name,CreativeFilePath,ApiType,extlTrackerPX1,extlTrackerPX2,extlTrackerScrpt1,extlTrackerScrpt2,clkThrURL): #name,Path,apiType,extlTrackerPX1,extlTrackerPX2,extlTrackerScrpt1,extlTrackerScrpt2,clkThrURL
        creativeBtn = WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-adgCreatives-newCreative']"))) #creative button
        creativeBtn.click() #clicking on the new creative button
        sleep(2)
        ImageTabBtn=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Image')]"))) 
        #click on Image tab
        driver.execute_script("arguments[0].click();",ImageTabBtn)

        # testing name under Image tab
        Creativename=driver.find_element(By.ID,"inp-creativesModal-creativeName")
        if Creativename.get_attribute('type')=='text':
            Creativename.click()
            Creativename.clear()
            Creativename.send_keys(name) # name 
        else:
            print('Failed, creative name is not of type text',Creativename.get_attribute('type'))

        # testing all labels name under the Image tab
        ImageTabLbls=driver.find_elements(By.XPATH,"//div[@id='modal--adgroup-new-creative']//label")
        acutalImageTabLbls=['Name', 'API Type', 'External Trackers (Pixels)', 'External Trackers (Scripts) or MRAID.js', 'Click-through URL']
        expectedImageTabLbls=[]
        for lbl in ImageTabLbls:
            expectedImageTabLbls.append(lbl.text)
        if collections.Counter(acutalImageTabLbls) == collections.Counter(expectedImageTabLbls):
            print('Passed, all labels under the Image tab are correct')
        else:
            print('Failed, all labels under the Image tab are incorrect',expectedImageTabLbls)
        
        # upload creative Image container text
        uplCreHeading=driver.find_element(By.XPATH,"//h3[contains(text(),'Upload')]")

        # Upload Creative Image test
        if uplCreHeading.tag_name == 'h3' and uplCreHeading.text == 'Upload Creative Image':
            print('Passed,',uplCreHeading.text,'is of ',uplCreHeading.tag_name,'tag')
        else:
            print('Failed,',uplCreHeading.text,'is of ',uplCreHeading.tag_name,'tag')   
        dragNdropText=driver.find_element(By.XPATH,"//div[contains(text(),'Drag and drop creative here')]")
        if dragNdropText.text == 'Drag and drop creative here':
            print('Passed,',dragNdropText.text,'is correct')
        else:
            print('Failed,',dragNdropText.text,'is incorrect')
        orText=driver.find_element(By.XPATH,"//div[@class='or']")
        if orText.text=='OR':
            print('Passed,',orText.text,'is correct')
        else:
            print('Failed,',orText.text,'is incorrect')
        UploadCreativeBoldContent=driver.find_elements(By.XPATH,"//div[@class='drop-box-msg']/b")
        actualCreativeBoldContent=['Please upload one of these sizes (in pixels). Double dimensions for retina mobile screens.','Other supported sizes include:']
        ExpectedCreativeBoldContent=[]
        for bold in UploadCreativeBoldContent:
            ExpectedCreativeBoldContent.append(bold.get_attribute('innerHTML'))
        if collections.Counter(actualCreativeBoldContent) == collections.Counter(ExpectedCreativeBoldContent):
            print('Passed, Bold content under the creative upload is correct')
        else:
            print('Failed, Bold content under the creative upload is incorrect',ExpectedCreativeBoldContent)

        UploadCreativePContent=driver.find_elements(By.XPATH,"//div[@class='drop-box-msg']/p")
        actualCreativePContent=['320x50, 300x250, 320x480, 728x90 sizes reach more than 95% of mobile inventory.','600x300, 720x240, 640x213, 640x160, 640x320, 300x50, 480x320, 768x1024, 1024x768, 640x960, 640x360 and 160x600.']
        ExpectedCreativePContent=[]
        for p in UploadCreativePContent:
            ExpectedCreativePContent.append(p.get_attribute('innerHTML'))
        if collections.Counter(actualCreativePContent) == collections.Counter(ExpectedCreativePContent):
            print('Passed, P content under the creative upload is correct')
        else:
            print('Failed, P content under the creative upload is incorrect',ExpectedCreativePContent)     

        # upload file path
        filePath=driver.find_element(By.XPATH,"//ng-form[@name='uploadImageCreativeForm']//input[@type='file']")
        filePath.send_keys(CreativeFilePath) 
        sleep(5)
        # testing the Api type selection box
        apiType=driver.find_element(By.ID,'inp-creativeModalImage-apiTypeSelect')
        select=Select(apiType)
        if len(select.options) == 6:
            print('Passed, options count under the Api dropdown is correct')
        else:
            print('Failed, options count under the Api dropdown is incorrect')
        
        # select script API Type
        apiType=driver.find_element(By.ID,'inp-creativeModalImage-apiTypeSelect')
        select=Select(apiType) 
        # testing all options text inside the API
        actualImageApiList=['None', 'VPAID1', 'VPAID2', 'MRAID1', 'MRAID2', 'ORMMA']
        expectedImageApiList=[]
        for option in select.options:
            expectedImageApiList.append(option.text)
        if collections.Counter(actualImageApiList) == collections.Counter(expectedImageApiList):
            print('Passed, under Image tab, API Type options are correct')
        else:
            print('Failed, under Image tab, API Type options are incorrect',expectedImageApiList)
        print('Image API options,',expectedImageApiList)

        # testing default value of api type
        if select.first_selected_option.text == 'MRAID2':
            print('Passed, default options under the Api dropdown is correct')
        else:
            print('Failed, default options under the Api dropdown is incorrect:',select.first_selected_option.text)
        # selecting explicity value in api dropdown
        select.select_by_value(ApiType) # dynamic API value 

        # # testing External Trackers (Pixels)
        externelTracker=driver.find_element(By.XPATH,"//xad-list-input[@label='External Trackers (Pixels)']//input")
        externelTracker.send_keys(extlTrackerPX1 , Keys.RETURN) 
        externelTracker.send_keys(extlTrackerPX2 , Keys.RETURN)
        sleep(2)

        # testing removing of last tracker
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//xad-list-input[@label='External Trackers (Pixels)']/ul[@class='submitted-items']/li[last()]/button"))).click()
        print('removed the last tracker from External Trackers (Pixels)')

        # testing External Trackers (Scripts) or MRAID.js
        externelTracker=driver.find_element(By.XPATH,"//xad-list-input[@label='External Trackers (Scripts) or MRAID.js']//input")
        externelTracker.send_keys(extlTrackerScrpt1 , Keys.RETURN)
        externelTracker.send_keys(extlTrackerScrpt2 , Keys.RETURN)
        sleep(2)
        # testing removing of last tracker
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//xad-list-input[@label='External Trackers (Scripts) or MRAID.js']/ul[@class='submitted-items']/li[last()]/button"))).click()
        print('removed the last tracker from External Trackers (Scripts) or MRAID.js')
        
        #scrolling the page down
        actions=ActionChains(driver)
        # actions.move_to_element().perform()
        elementPosition=driver.find_element(By.ID,'btn-creativesModal-newCreativeSave')
        actions=ActionChains(driver)
        actions.move_to_element(elementPosition).perform()
 
        # testing Click-through URL*
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//form[@name='uploadTabCreativeForm']//input[@id='inp-creativeModalImage-clickThroughURL']"))).send_keys(clkThrURL) 

        # testing creative footer-subtext and link address 
        creativeFooter=driver.find_element(By.XPATH,"//p[@class='footer-subtext']")
        terms="By clicking Save, I agree to comply in all respects with the MMA Mobile Advertising Guidelines and GroundTruth's Content Guidelines."
        if creativeFooter.text == terms:
            print('Passed, creative terms are correct')
        else:
            print('Failed, creative terms are incorrect')
        creativeFooterLink=driver.find_element(By.LINK_TEXT,"GroundTruth's Content Guidelines")
        if creativeFooterLink.get_attribute('href') == "https://www.groundtruth.com/guidelines/":
            print('Passed, creative footer link is correct') 
        else:
            print('Failed, creative footer link is incorrect')
       
        # moving to the bottom of the page
        actions.move_to_element(elementPosition).perform()

        # testing count of buttons
        creativeFooterButtons=driver.find_elements(By.XPATH,"//div[@class='footer-buttons']/button")
        # testing creative footer btn count
        if len(creativeFooterButtons) == 2:
            print('Passed, button count are correct')
        else:
            print('Failed, button count are incorrect',len(creativeFooterButtons))
        actualCreativeFooterButtons=['Cancel', 'Save']
        expectedCreativeFooterButtons=[]
        for btn in creativeFooterButtons:
            expectedCreativeFooterButtons.append(btn.text)
        if collections.Counter(actualCreativeFooterButtons) == collections.Counter(expectedCreativeFooterButtons):
            print('Passed, buttons names under creative footer are correct')
        else:
            print('Failed, buttons names under creative footer are incorrect',expectedCreativeFooterButtons)

        # clicking on Cancel or Save button
        # driver.find_element(By.XPATH,"//div[@class='footer-buttons']//button[contains(text(),'Cancel')]").click()
        # uncomment for save button
        driver.find_element(By.XPATH,"//span[contains(text(),'Save')]").click()

    def ScriptCreative(self,name,scriptTagCreative,Size,ApiType,extlTrackerPX1,extlTrackerPX2,extlTrackerScrpt1,extlTrackerScrpt2,clkThrURL):
        sleep(5)
        creativeBtn = WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-adgCreatives-newCreative']"))) #creative button
        creativeBtn.click() #clicking on the new creative button
        sleep(2)
        # scriptPosition=driver.find_element(By.XPATH,"//a[contains(text(),'Script')]")
        actions=ActionChains(driver)
        # actions.move_to_element(scriptPosition).perform()
        scriptTabBtn=WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Script')]"))) 
        # click on SCRIPT tab
        driver.execute_script("arguments[0].click();",scriptTabBtn)
       
        # all labels under the script tab
        scriptTabLbls=driver.find_elements(By.XPATH,"//div[@id='modal--adgroup-new-creative']//label") 
        acutalScriptTabLbls=['Name', 'Script tag*', 'Size*', 'Script API Type', 'External Trackers (Pixels)', 'External Trackers (Scripts) or MRAID.js', 'Click-through URL']
        expectedScriptTabLbls=[]
        for lbl in scriptTabLbls:
            expectedScriptTabLbls.append(lbl.text)
        if collections.Counter(acutalScriptTabLbls) == collections.Counter(expectedScriptTabLbls):
            print('Passed, all labels under the Script tab are correct')
        else:
            print('Failed, all labels under the Script tab are incorrect',expectedScriptTabLbls)
        
        # testing  script creative name filed
        CreativeName=driver.find_element(By.ID,"inp-creativesModal-creativeName")
        if CreativeName.get_attribute('type') == 'text':
            CreativeName.click()
            CreativeName.clear()
            CreativeName.send_keys(name) #name of scritp
            sleep(2)
        else:
            print('Failed, Creative name field is not of text type',CreativeName.get_attribute('type'))
        
        # testing script tag
        scriptTag= driver.find_element(By.ID,'inp-creativeModalScript-scriptTag')
        if scriptTag.get_attribute('value')=='':
            scriptTag.send_keys(scriptTagCreative)
            print('passed, script tag is empty')
            sleep(2)
            uploadScript=driver.find_element(By.ID,"btn-creativeModalScript-scriptUpload")
            if uploadScript.text=='Load Creative':
                uploadScript.click()
                print('Load creative text is correct')
                print('clicked on upload')
            else:
                print('Load creative text is incorrect',uploadScript.text)
        else:
            print('Failed script tag is non-empty')
            
        # testing the size* selection box
        size=driver.find_element(By.ID,'inp-creativeModalScript-size')
        select=Select(size)
        # testing options under size drop-down
        actualScriptSizeList=['300x600', '160x600', '600x300', '720x240', '640x213', '640x160', '728x90', '300x50', '300x250', '320x50', '300x250 (Interstitial size)', '320x480 (Interstitial size)', '480x320 (Interstitial size)', '768x1024 (Interstitial size)', '1024x768 (Interstitial size)', '640x960 (Interstitial size)']
        expectedScriptSizeList=[]
        # for sizelist in scriptSizeList:
        for option in select.options:
            expectedScriptSizeList.append(option.text)
        if collections.Counter(actualScriptSizeList) == collections.Counter(expectedScriptSizeList):
            print('Passed, Options under Script tab is correct')
        else:
            print('Failed, Options under Script tab is incorrect',expectedScriptSizeList)
        # print('size dropdown list',expectedScriptSizeList)

        # testing length of size drop-down
        if len(select.options) == 16:
            print('Passed, options count under the Size dropdown is correct')
        else:
            print('Failed, options count under the Size dropdown is incorrect',len(select.options))
         
        # testing default value of api type
        if select.first_selected_option.text == '300x600':
            print('Passed, default options under the Api dropdown is correct')
        else:
            print('Failed, default options under the Api dropdown is incorrect:',select.first_selected_option.text)
        # selecting explicity value in api dropdown
        select.select_by_value(Size)

        # select script API Type
        apiType=driver.find_element(By.ID,'inp-creativeModalScript-apiTypeSelect')
        select=Select(apiType)
        # testing the options text inside the API
        actualScriptApiList=['None', 'VPAID1', 'VPAID2', 'MRAID1', 'MRAID2', 'ORMMA']
        expectedScriptApiList=[]
        for option in select.options:
            expectedScriptApiList.append(option.text)
        if collections.Counter(actualScriptApiList) == collections.Counter(expectedScriptApiList):
            print('Passed, under Script tab, Script API Type options are correct')
        else:
            print('Failed, under Script tab, Script API Type options are incorrect',expectedScriptApiList)

        # testing the count of options
        if len(select.options) == 6:
            print('Passed, options count under the Api dropdown is correct')
        else:
            print('Failed, options count under the Api dropdown is incorrect',len(select.options))

        # testing default value of api type
        if select.first_selected_option.text == 'MRAID2':
            print('Passed, default options under the Api dropdown is correct')
        else:
            print('Failed, default options under the Api dropdown is incorrect:',select.first_selected_option.text)

        # selecting explicity value in api dropdown
        select.select_by_value(ApiType)

        #  testing External Trackers (Pixels)
        externelTracker=driver.find_element(By.XPATH,"//xad-list-input[@label='External Trackers (Pixels)']//input")
        externelTracker.send_keys(extlTrackerPX1 , Keys.RETURN)
        externelTracker.send_keys(extlTrackerPX2 , Keys.RETURN)
        sleep(2)
        # testing removing of last tracker
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//xad-list-input[@label='External Trackers (Pixels)']/ul[@class='submitted-items']/li[last()]/button"))).click()
        print('removed the last tracker from External Trackers (Pixels)')

        # testing External Trackers (Scripts) or MRAID.js
        externelTracker=driver.find_element(By.XPATH,"//xad-list-input[@label='External Trackers (Scripts) or MRAID.js']//input")
        externelTracker.send_keys(extlTrackerScrpt1 , Keys.RETURN)
        externelTracker.send_keys(extlTrackerScrpt1 , Keys.RETURN)
        sleep(2)
        # testing removing of last tracker
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//xad-list-input[@label='External Trackers (Scripts) or MRAID.js']/ul[@class='submitted-items']/li[last()]/button"))).click()
        print('removed the last tracker from External Trackers (Scripts) or MRAID.js')
       
        # moving to the bottom of the page
        actions.move_to_element(driver.find_element(By.ID,"btn-creativesModal-newCreativeCancel")).perform()
        sleep(2)

        # testing Click-through URL*
        driver.find_element(By.XPATH,"//form[@name='uploadTabCreativeForm']//input[@id='clickThroughURLField']").send_keys(clkThrURL)

        # testing creative footer-subtext and link address 
        creativeFooter=driver.find_element(By.XPATH,"//p[@class='footer-subtext']")
        terms="By clicking Save, I agree to comply in all respects with the MMA Mobile Advertising Guidelines and GroundTruth's Content Guidelines."
        if creativeFooter.text == terms:
            print('Passed, creative terms are correct')
        else:
            print('Failed, creative terms are incorrect')
        creativeFooterLink=driver.find_element(By.LINK_TEXT,"GroundTruth's Content Guidelines")
        if creativeFooterLink.get_attribute('href') == "https://www.groundtruth.com/guidelines/":
            print('Passed, creative footer link is correct') 
        else:
            print('Failed, creative footer link is incorrect')

        # testing count of buttons
        creativeFooterButtons=driver.find_elements(By.XPATH,"//div[@class='footer-buttons']/button")
        # testing creative footer btn count
        if len(creativeFooterButtons) == 2:
            print('Passed, button count are correct')
        else:
            print('Failed, button count are incorrect',len(creativeFooterButtons))
        actualCreativeFooterButtons=['Cancel', 'Save']
        expectedCreativeFooterButtons=[]
        for btn in creativeFooterButtons:
            expectedCreativeFooterButtons.append(btn.text)
        if collections.Counter(actualCreativeFooterButtons) == collections.Counter(expectedCreativeFooterButtons):
            print('Passed, buttons names under creative footer are correct')
        else:
            print('Failed, buttons names under creative footer are incorrect',expectedCreativeFooterButtons)

        # clicking on Cancel or Save button
        # driver.find_element(By.XPATH,"//div[@class='footer-buttons']//button[contains(text(),'Cancel')]").click()
        # uncomment for save button
        driver.find_element(By.XPATH,"//span[contains(text(),'Save')]").click()

    def VideoCreative(self,name,VastTag,ApiType,extlTrackerPX1,extlTrackerPX2,clkThrURL):#name,VastTag,ApiType,extlTrackerPX1,extlTrackerPX2,clkThrURL
        sleep(5)
        creativeBtn=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-adgCreatives-newCreative']"))) #creative button
        creativeBtn.click() #clicking on the new creative button
        sleep(2)
        VideoTab = WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Video')]")))
        VideoTab.click()
        print('clicked on video tab')
        print(VideoTab.text)
        if VideoTab.text=='VIDEO':
            # wait=WebDriverWait(driver,40)
            VideoName=driver.find_element(By.ID,"inp-creativesModal-creativeName")
            VideoName.clear()
            VideoName.send_keys(name) # 
        
            # testing all labels under the video tab
            videoTabLbls=driver.find_elements(By.XPATH,"//div[@id='modal--adgroup-new-creative']//label") 
            acutalVideoTabLbls=['Name', 'VAST Tag URL*', 'API Type', 'External Impression Trackers (Pixels)', 'Click-through URL']
            expectedVideoTabLbls=[]
            for lbl in videoTabLbls:
                expectedVideoTabLbls.append(lbl.text)
            if collections.Counter(acutalVideoTabLbls) == collections.Counter(expectedVideoTabLbls):
                print('Passed, all labels under the Video tab are correct')
            else:
                print('Failed, all labels under the Video tab are incorrect',expectedVideoTabLbls)

            # testing Load video button before entering the vast tag url
            beforeXML=driver.find_element(By.ID,"btn-creativeModalVideo-Videopload")
            if beforeXML.is_enabled()==False and beforeXML.text=='Load Video':
                print('Passed, Load Video button text is correct and it is disabled before entering vast tag url by default')
            else:
                print('Failed, Load Video button text is incorrect and it is enabled before entering vast tag url by default',beforeXML.text)

            # testing VAST tag URL
            vastTag= driver.find_element(By.ID,'inp-creativeModalVideo-vastField')
            if vastTag.get_attribute('value')=='':
                print('passed, Vast tag is empty')
                vastTag.send_keys(VastTag) 
                # testing Load video button after entering the vast tag url
                # driver.find_element(By.XPATH,"//button[@id='btn-creativeModalVideo-Videopload']").click()
                WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.ID,"btn-creativeModalVideo-Videopload"))).click()
                sleep(2)
                print('clicked on load button')
            else:
                print('Failed Vast tag is non-empty')        
            sleep(5)

            # testing interstitial
            interstitial=driver.find_element(By.XPATH,"//input[@ng-model='creativeInterstitial']/../div[@class='title']")
            if interstitial.text=='Interstitial':
                print('Passed, interstitial text is correct')
                driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH,"//input[@type='checkbox' and @ng-model='creativeInterstitial']")) #interstitial.click()
                print('clicked on interstitial button')
                sleep(5)
            else:
                print('Failed, interstitial text is incorrect or unable to click on button')
        else:
            print('video tab is not found@!')

        # select script API Type
        apiType=driver.find_element(By.ID,'inp-creativeModalVideo-apiTypeSelect')
        select=Select(apiType)
        # testing the options text inside the API
        actualScriptApiList=['None', 'VPAID1', 'VPAID2', 'MRAID1', 'MRAID2', 'ORMMA']
        expectedScriptApiList=[]
        for option in select.options:
            expectedScriptApiList.append(option.text)
        if collections.Counter(actualScriptApiList) == collections.Counter(expectedScriptApiList):
            print('Passed, under Script tab, Script API Type options are correct')
        else:
            print('Failed, under Script tab, Script API Type options are incorrect',expectedScriptApiList)

        # testing the count of options
        if len(select.options) == 6:
            print('Passed, options count under the Api dropdown is correct')
        else:
            print('Failed, options count under the Api dropdown is incorrect',len(select.options))

        # testing default value of api type
        if select.first_selected_option.text == 'MRAID2':
            print('Passed, default options under the Api dropdown is correct')
        else:
            print('Failed, default options under the Api dropdown is incorrect:',select.first_selected_option.text)
        # selecting explicity value in api dropdown
        select.select_by_value(ApiType) 
        
        #  testing External Trackers (Pixels)
        externelTracker=driver.find_element(By.ID,"impressions-urls")
        externelTracker.send_keys(extlTrackerPX1 , Keys.RETURN)
        externelTracker.send_keys(extlTrackerPX2 , Keys.RETURN)
        sleep(2)
        # testing removing of last tracker
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//ul[@class='submitted-items']/li[last()]/button"))).click()
        print('removed the last tracker from External Trackers (Pixels)')

        # moving to the bottom of the page
        actions=ActionChains(driver)
        actions.move_to_element(driver.find_element(By.ID,"btn-creativesModal-newCreativeCancel")).perform()
        sleep(2)

        # testing Click-through URL*
        driver.find_element(By.XPATH,"//form[@name='uploadTabCreativeForm']//input[@id='inp-creativeModalVideo-clickThroughURLField']").send_keys(clkThrURL)
        
        # testing creative footer-subtext and link address 
        creativeFooter=driver.find_element(By.XPATH,"//p[@class='footer-subtext']")
        terms="By clicking Save, I agree to comply in all respects with the MMA Mobile Advertising Guidelines and GroundTruth's Content Guidelines."
        if creativeFooter.text == terms:
            print('Passed, creative terms are correct')
        else:
            print('Failed, creative terms are incorrect')
        creativeFooterLink=driver.find_element(By.LINK_TEXT,"GroundTruth's Content Guidelines")
        if creativeFooterLink.get_attribute('href') == "https://www.groundtruth.com/guidelines/":
            print('Passed, creative footer link is correct') 
        else:
            print('Failed, creative footer link is incorrect')

        # testing count of buttons
        creativeFooterButtons=driver.find_elements(By.XPATH,"//div[@class='footer-buttons']/button")
        # testing creative footer btn count
        if len(creativeFooterButtons) == 2:
            print('Passed, button count are correct')
        else:
            print('Failed, button count are incorrect',len(creativeFooterButtons))
        actualCreativeFooterButtons=['Cancel', 'Save']
        expectedCreativeFooterButtons=[]
        for btn in creativeFooterButtons:
            expectedCreativeFooterButtons.append(btn.text)
        if collections.Counter(actualCreativeFooterButtons) == collections.Counter(expectedCreativeFooterButtons):
            print('Passed, buttons names under creative footer are correct')
        else:
            print('Failed, buttons names under creative footer are incorrect',expectedCreativeFooterButtons)

        # clicking on Cancel or Save button
        # driver.find_element(By.XPATH,"//div[@class='footer-buttons']//button[contains(text(),'Cancel')]").click()
        # uncomment for save button
        driver.find_element(By.XPATH,"//span[contains(text(),'Save')]").click() 


    def HTMLCreative(self,name,BusName,Caption,clkThrURL):#name,BusName,Caption,clkThrURL
        sleep(5)
        creativeBtn=WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-adgCreatives-newCreative']"))) #creative button
        creativeBtn.click() #clicking on the new creative button
        sleep(2)
        HTMLTab = WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'HTML5')]")))
        HTMLTab.click()
        print('clicked on HTML5 tab')
        print(HTMLTab.text)

        if HTMLTab.text=='HTML5':
            # wait=WebDriverWait(driver,40)
            VideoName=driver.find_element(By.ID,"inp-creativesModal-creativeName")
            VideoName.clear()
            VideoName.send_keys(name) #name 
            
            # testing all labels under the video tab
            HtmlTabLbls=driver.find_elements(By.XPATH,"//div[@id='modal--adgroup-new-creative']//label") 
            acutalHtmlTabLbls=['Name', 'Business Name', 'Caption', 'Click-through URL']
            expectedHtmlTabLbls=[]
            for lbl in HtmlTabLbls:
                expectedHtmlTabLbls.append(lbl.text)
            if collections.Counter(acutalHtmlTabLbls) == collections.Counter(expectedHtmlTabLbls):
                print('Passed, all labels under the Video tab are correct')
            else:
                print('Failed, all labels under the Video tab are incorrect',expectedHtmlTabLbls)
                
            
            htmlBusName=driver.find_element(By.ID,'inp-creativeModalHTML-businessName')
            htmlBusName.send_keys(BusName) #test if is empty or not
            htmlcaption=driver.find_element(By.ID,"inp-creativeModalHTML-caption")
            htmlcaption.send_keys(Caption)
            htmlclkThrURL=driver.find_element(By.ID,"inp-creativeModalHTML-clickThroughURLField")
            htmlclkThrURL.send_keys(clkThrURL)
        else:
            print('HTML5 tab is not available')

        # testing creative footer-subtext and link address 
        creativeFooter=driver.find_element(By.XPATH,"//p[@class='footer-subtext']")
        terms="By clicking Save, I agree to comply in all respects with the MMA Mobile Advertising Guidelines and GroundTruth's Content Guidelines."
        if creativeFooter.text == terms:
            print('Passed, creative terms are correct')
        else:
            print('Failed, creative terms are incorrect')
        creativeFooterLink=driver.find_element(By.LINK_TEXT,"GroundTruth's Content Guidelines")
        if creativeFooterLink.get_attribute('href') == "https://www.groundtruth.com/guidelines/":
            print('Passed, creative footer link is correct') 
        else:
            print('Failed, creative footer link is incorrect')

        # testing count of buttons
        creativeFooterButtons=driver.find_elements(By.XPATH,"//div[@class='footer-buttons']/button")
        # testing creative footer btn count
        if len(creativeFooterButtons) == 2:
            print('Passed, button count are correct')
        else:
            print('Failed, button count are incorrect',len(creativeFooterButtons))
        actualCreativeFooterButtons=['Cancel', 'Save']
        expectedCreativeFooterButtons=[]
        for btn in creativeFooterButtons:
            expectedCreativeFooterButtons.append(btn.text)
        if collections.Counter(actualCreativeFooterButtons) == collections.Counter(expectedCreativeFooterButtons):
            print('Passed, buttons names under creative footer are correct')
        else:
            print('Failed, buttons names under creative footer are incorrect',expectedCreativeFooterButtons)

        # clicking on Cancel or Save button
        # driver.find_element(By.XPATH,"//div[@class='footer-buttons']//button[contains(text(),'Cancel')]").click()
        # uncomment for save button
        driver.find_element(By.XPATH,"//span[contains(text(),'Save')]").click() 


c=campaignSetUp()
c.NewCampaignButton()
c.NewCampaignModel('Regression-Automation-testing-'+str(random.randint(1,100)),'Pet Services','campaign-budget','Save')# 'adgroup-budget','campaign-budget','×','Save'
c.TargettingHeader()
c.deviceType()
# c.LeftHandDetails()
# c.RightHandDetials()
# c.AdGroupHeader()
c.AdGroupSetUp() 
c.selectAudience('Millennials','Potato Growers','Live Nation',"Costco",'Hispanics','Vegetable Farms','Pizza Hut','Renault')#Behavior,Category,LocationGroup,Brand #"Wendy's" "7-Eleven"
# c.additionalLocationFilter()
# c.DriveToDestinationt()
# c.Demographics()
# c.deviceTargeting()
# c.OptimizationStrategy()
# c.publisherCategory()
c.BuildCustomAudience()
cr=Createives()
cr.CreativeDetailsVerify()
cr.newCreativeDetails()
cr.ImageCreative('Default Image','/Users/surenderpal/Downloads/Creatives/4.jpg','ORMMA','https://ads-release-3-17-np.groundtruth.com/','https://ads-release-3-17-np.groundtruth.com/','https://ads-release-3-16-np.groundtruth.com/','https://ads-release-3-16-np.groundtruth.com/','https://www.groundtruth.com/') #name,Path,apiType,extlTrackerPX1,extlTrackerPX2,extlTrackerScrpt1,extlTrackerScrpt2,clkThrURL
cr.ScriptCreative('Script',"<ins class='dcmads' style='display:inline-block;width:320px;height:50px' data-dcm-placement='N4789.3009684GROUNDTRUTH.COM/B23990316.271139896' data-dcm-rendering-mode='script' data-dcm-https-only data-dcm-resettable-device-id='%%USER_UID_OPTOUT%%' data-dcm-click-tracker='%%ENCODED_CLICKURL%%' data-dcm-landing-page-escapes=0> <script src='https://www.googletagservices.com/dcm/dcmads.js'></script> </ins>",'string:300x50_0','MRAID1','https://ads-release-3-17-np.groundtruth.com/','https://ads-release-3-17-np.groundtruth.com/','https://ads-release-3-16-np.groundtruth.com/','https://ads-release-3-16-np.groundtruth.com/','www.groundtruth.com') #name,scriptTagCreative,Size,ApiType,extlTrackerPX1,extlTrackerPX2,extlTrackerScrpt1,extlTrackerScrpt2,clkThrURL
cr.VideoCreative('Video','https://cf.groundtruth.com/swift/2019/11/21/c2a40c8d-989b-4ff4-922e-535c07f35c05.xml','VPAID2','https://ads-release-3-16-np.groundtruth.com/','https://ads-release-3-16-np.groundtruth.com/','https://www.groundtruth.com/') #name,VastTag,ApiType,extlTrackerPX1,extlTrackerPX2,clkThrURL
cr.HTMLCreative('HTML','Groundtruth','Adtech Domain','www.groundtruth.com') #name,BusName,Caption,clkThrURL
sleep(20)
driver.close() 

# Failed,After click On Auto Checkbox CTR THRESHOLD 0% is incorrect
# Failed, default value inside the input box is incorrect and value is: 0
# . Is there a way to type in a textbox without using sendKeys()?
# driver.execute_script("document.getElementById('q').value='value here'")

# from selenium import webdriver
# chrome_driver_path = "D:\\drivers\\chromedriver.exe"
# driver=webdriver.Chrome(chrome_driver_path)
# import requests
# for link in links:
#     r = requests.head(link)
#     if r.status_code!=404:
#          driver.get(link)
#     else:
#           print(str(link) + " isn't available.")