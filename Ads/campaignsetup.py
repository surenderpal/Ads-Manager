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
        if info.get_attribute('uib-popover') == 'Note: you can add other types of tactics to your campaign as you continue through your set up.':
            print('Passed, tooltip under the targeting tactics is correct')
        else:
            print('Failed, tooltip under the targeting tactics is Incorrect',info.get_attribute('uib-popover'))

        noOftactics =  driver.find_elements(By.XPATH, "//div[@class='targeting-goals-view ng-scope']/ul/li")
        print('Count of tactics available is',len(noOftactics))
        tactisRadioButtonHeading=driver.find_elements(By.XPATH, "//div[@class='targeting-goals-view ng-scope']/ul/li//h3") # radio button headings
        # tactisRadioButtonHeadingp = driver.find_elements(By.XPATH, "//div[@class='targeting-goals-view ng-scope']/ul/li//p") #tactics parag
        # onPremiseP = ""
        # locationP='"Send ads to people in real-time based on where they are e.g. People who are inside a fast food restaurant"'
        print('%' * 50)
        tactics = driver.find_elements(By.XPATH, "//div[@class='goal-label']/h3")
        for tactic in tactics:
            tacticOption= 'Target by Audience' #Location
            tacticOption2 = 'Target by Audience' #Audience,Weather
            if tactic.text == tacticOption: #if tactic name is Location Target by Weather, Target by Audience
                # driver.find_element(By.XPATH, "//h4[text()='On Premise Targeting']").click()
                print('Target by Location Paragraph:',driver.find_element(By.XPATH, "//div[@class='goal-label']/p").text)
                tactic.click()
                subTactic= 'On Premise Targeting' # On Premise Targeting,Neighborhoods,Geotargets
                print('Sub tactics count inside Target by Location:',len(driver.find_elements(By.XPATH,"//h4[contains(text(),'')]"))-1)
                driver.find_element(By.XPATH,"//h4[contains(text(),'"+subTactic+"')]").click()
                print(driver.find_element(By.XPATH,"//div[@class='sub-option-text']/p").text)
                break
            else:
                driver.find_element(By.XPATH, "//h3[contains(text(),'"+tacticOption2+"')]").click()
                print(driver.find_element(By.XPATH, "//div[@class='goal-label']/p").text)
                break       

c=campaignSetUp()
c.NewCampaignButton()
c.NewCampaignModel('Regression-Automation-testing','Pet Services','campaign-budget','Save')# 'adgroup-budget','campaign-budget','×','Save'
c.TargettingHeader()
sleep(20)
driver.close()
