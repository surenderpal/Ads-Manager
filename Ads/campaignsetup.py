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
    def NewCampaignModel(self,CampaignName,categoryName,BudgetType): #campaignAction
        '''
        this function is created by surender pal, it opens the campaign creation model, and fills the form,
        campaignName is the name of campaign that user creates, campaign name can be anything.
        categoryname is the name of category that user selects, user has to select from list,
        BudgetType is the type of budget that user selects. budget can be of two types Ad Group and Campaign level #adgroup, campaign
        BudgetType value="campaign-budget" , value="adgroup-budget" 
        campaignAction is either 'Save' or '×'
        '''
        # infoText='''A budget is the amount of money you want to spend on showing people your ads.Campaign budget is a budget you set once at the campaign level. The campaign budget will be shared across ad groups based on available inventory that each ad group is competing for. Spending will not be evenly divided across all ad groups.Ad group budgets are set for each ad group, when you setup the targeting tactics. This provides more granular budget control but has the risk of under delivery. You also have the option to convert ad group budgets to a single campaign budget after launching the campaign.'''
        ToolTipText = '''A budget is the amount of money you want to spend on showing people your ads. 

 Campaign budget is a budget you set once at the campaign level. The campaign budget will be shared across ad groups based on available inventory that each ad group is competing for. Spending will not be evenly divided across all ad groups. 

 Ad group budgets are set for each ad group, when you setup the targeting tactics. This provides more granular budget control but has the risk of under delivery. You also have the option to convert ad group budgets to a single campaign budget after launching the campaign.'''
        actions=ActionChains(driver)
        ModelTitle = driver.find_element(By.XPATH, "//div[@id='modal--create-new-campaign']//div[text()='Create new campaign']") #model title
        # labels that are listed in campaign creation model
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
                driver.find_element(By.ID, "inp-createCampModal-campName").send_keys('CampaignName') #campaign name 
                if CategoryLabelName == 'Category':
                    print('Passed, Category Name Label is correct!!')
                    if category.get_attribute('placeholder') == 'Search and select a category':
                        print('Passed!!,Placeholder inside Category')
                        category.click()
                        sleep(2)
                        category_li = driver.find_elements(By.XPATH, "//div[@class='gt-autocomplete-dropdown ng-scope']/ul/li")
                        print('Count of category:',len(category_li))
                        for li in category_li:
                            print(li.text)
                        driver.find_element(By.XPATH,"//li[contains(text(),'"+categoryName+"')]").send_keys(categoryName)# category name:- Potato Growers
                    else:
                        print('Failed!!,Placeholder inside Category')
                else:
                    print('Failed, Category Name lable is Incorrect') 
            else:
                print('Failed, Campaign Name lable is Incorrect')
            # print(BudgetSetting)

            # print(budgetSetting)# budgetSetting = Budget Setting
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
                    # code for select budget
                    for budget in budgets:
                        print(budget.get_attribute('value'))
                        if BudgetType == 'adgroup-budget':
                            driver.find_element(By.ID, "btn-campaignCreateModal-submit").click()
                        else:
                            if BudgetType == 'campaign-budget':
                                    driver.find_element_by_xpath("//input[@value='campaign-budget']").click()
                                    note = driver.find_element(By.XPATH, '//p').text #Note warning inside campaign budget
                                    if note == 'Note: Selecting this options does not guarantee even budget distribution amongst each ad group. Once saved, this setting cannot be changed.':
                                        print('Passed, campaign Note!!, Note is: ',note)
                                        driver.find_element(By.NAME, "budgetField").clear()
                                        driver.find_element(By.NAME, "budgetField").send_keys('10')
                                        # driver.find_element(By.ID, "btn-campaignCreateModal-submit").click()
                                        # driver.find_element(By.XPATH, "//button/span[contains(text(),'Save')]").click()
                                    else:
                                        print('Failed, campaign Note!!')
                            else:
                                print('Failed, Wrong budget selected!!')
                            break
                     # action to save or to close 
                    sleep(2)
                    # driver.find_element(By.XPATH, "//button/span[contains(text(),'"+campaignAction+"')]").click()
                    # print('clicked on campaign creation action:',campaignAction)
                    driver.find_element(By.XPATH, "//button/span[contains(text(),'×')]").click()
                else:
                    print('Failed, info tool tip text is Incorrect')
            else:
                print('Failed, budget setting label text is Incorrect')
        else:
            print('Failed, Model title!!')
        

c=campaignSetUp()
c.NewCampaignButton()
c.NewCampaignModel('Regression-Automation-testing','Pet Services','campaign-budget')#,'x'
sleep(60)
driver.close()
