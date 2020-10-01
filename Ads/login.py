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
driver.get('https://ads-release-3-15-np.groundtruth.com/')
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
A.login('surender.pal@groundtruth.com','Surenderpal@1991')

class TenantDashboard():
    wait=WebDriverWait(driver, 40)

    def links_Buttons(self):
        links=driver.find_elements(By.TAG_NAME,'a')
        print('Total link present on Tenant Dashboard page is:',len(links))
        for link in links:   
            print(link.text,link.get_attribute('href'))

        inputs=driver.find_elements(By.TAG_NAME,"input")
        print('Total no of input element present in Tenant Dashboard is:',len(inputs))

        for input in inputs:    
            print(input.get_attribute("placeholder"))

    def hamburger(self):
        wait=WebDriverWait(driver, 40)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu"))).click() #click on hamburger button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu-tenant-dashboard"))).click() #click on tenant dashboard
        print('clicked on Hamburger Menu..')
    
    def SelectTenant(self,TenName):
        wait=WebDriverWait(driver, 40)
        ''' Tenant selection '''
        wait.until(EC.element_to_be_clickable((By.XPATH ,"//label[text()='Tenant']/..//span[@class='dropdown-title ng-binding']"))).click() #tenant selection
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search-dropdown-list-Tenant']"))).send_keys(TenName) #passed tenant name in input box
        sleep(2)
        driver.find_element_by_xpath("//input[@id='Tenant-0']").click() #click on input box.
        sleep(5)
        print('Tenant selected: ',TenName)

    def SelectOrg(self,OrgName):
        wait=WebDriverWait(driver, 40)
        ''' Orgnization selection'''
        wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Organization']/..//span[@class='dropdown-title ng-binding']"))).click() # org selection
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search-dropdown-list-Organization']"))).send_keys(OrgName)
        sleep(2)
        driver.find_element_by_xpath("//input[@id='Organization-0']").click()
        sleep(5)
        print('Organization selected: ', OrgName)

    def SelectAccount(self,AccountName):
        wait=WebDriverWait(driver, 40)
        ''' Account selection '''
        wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Account']/..//span[@class='dropdown-title ng-binding']"))).click() #account selected
        wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='search-dropdown-list-Account']"))).send_keys(AccountName)
        sleep(2)
        driver.find_element_by_xpath("//input[@id='Account-0']").click()
        # driver.find_element(By.XPATH, "//input[@id='Account-0']").send_keys(Keys.ESCAPE)
        sleep(5)
        print('Account selection: ',AccountName)

    def TenantTitleSection(self):
        sleep(10)
        caption=driver.find_element(By.XPATH, "//div[contains(text(),'Dashboard')]").text
        # print(caption)
        if caption == 'Dashboard':
            print('Caption(Dashboard) is correct and passed!!')
        else:
            print('Caption(Dashboard) is incorrect and failed')
        
        TenantName=driver.find_element(By.XPATH, "//div[contains(text(),'Test Tenant')]").text
        if TenantName == 'Test Tenant': #how to create a dynamic value here for test tenant.
            print('Test passed, displayed tenant name is:',TenantName)
        else:
            print('Test failed, displayed tenant name is:',TenantName)

    def searchbox(self):
        sleep(10)
        searchCampaignInputBox=driver.find_element(By.XPATH, "//input[@id='inp-tenantDash-searchCampaign']")
        if searchCampaignInputBox.tag_name == 'input':
            print('Tag(input) is correct')
            searchCampaignInputBox.click()
            searchCampaignInputBox.clear()
            searchCampaignInputBox.send_keys('cpg')
            # emptyCampaignMessage = driver.find_element(By.XPATH, "//div[contains(text(),'There are no campaigns that match the selected fil')]").text
            # print(emptyCampaignMessage)

        else:
            print('Tag(input) is Incorrect')


        # searchBox=driver.find_element(By.ID, "inp-base-searchbox-new")
        # searchBox.click()
        # searchBox.send_keys('test',Keys.ENTER)
        # # driver.back()

        # DateCreated=driver.find_elements(By.XPATH, "//fieldset[@ng-show='searchFiltersUi.startDate.show']")
        # for date in DateCreated:
        #     print(date.text)
        # if driver.find_element(By.ID, "inp-search-dateCreated-all").get_attribute('type') =='radio':

        #     print('element is radio button and ')
        #     driver.find_element(By.ID, "inp-search-dateCreated-all").is_selectesd():
        #     driver.find_element(By.ID, "inp-search-dateCreated-all").get_attribute('')
        #     print('Default value selected is: ',)
        # driver.find_element(By.ID, "//input[@id='inp-search-dateCreated-week']").click()
        
    def TermAndPrivacyPolicy(self):
        sleep(10)
        terms=driver.find_element(By.ID, "btn-baseFooter-termsOfUse")
        if terms.tag_name == 'a':
            print('element is: ',terms.tag_name)
        else:
            print('element is not link it is: ',terms.tag_name)

        if terms.is_displayed() and terms.is_enabled()==True:
            terms.click()
            print(terms.text,'link is enabled, displayed and',terms.text,'link is clicked')
            sleep(2)
            element=driver.find_element(By.ID, 'btn-termsConditions-close')
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        else:
            print(terms.text,'Link is neither enable or displayed')

        privacy=driver.find_element(By.ID, 'btn-baseFooter-privacyPolicy')
        if privacy.tag_name== 'a':
            print(privacy.text)
        else:
            print(privacy.text,' it is not Link element')
        
        
        if privacy.is_displayed() and privacy.is_enabled() == True:
            privacy.click()
            sleep(5)
            print(privacy.text, 'Link is displayed, enabled and clicked')
            sleep(10)
            handle=driver.current_window_handle
            handles=driver.window_handles
            for handle in handles:
                driver.switch_to.window(handle)
                sleep(1)
                if driver.title=='Privacy Policy - GroundTruth - GroundTruth':
                    print('Closed window title is: ',driver.title)
                    driver.close()
                    break     
            driver.switch_to.window(handle)            
        else:
            print(privacy.text,'Link is neither enable or displayed')

    def LiveToDate(self,To,From,action,actiontype):
        '''
        applyBtn has actiontype = success  
        cancelBtn has actiontype = default 
        '''
        sleep(5)
        driver.find_element(By.NAME,'daterange').click()
        driver.find_element(By.NAME,'daterangepicker_start').clear()
        driver.find_element(By.NAME,'daterangepicker_start').send_keys(To) 
        driver.find_element(By.NAME,'daterangepicker_end').clear()    
        driver.find_element(By.NAME,'daterangepicker_end').send_keys(From) 
        sleep(2)
        driver.find_element(By.XPATH,"//button[@class='"+action+" btn-sm btn-"+actiontype+"']").click() 
        print('Button clicked in Live to date functionaliy is ',actiontype,'applyBtn has actiontype = success and cancelBtn has actiontype = default')
        sleep(5)

    def campaignStatusFilter(self,filterType):
        '''
        filter type has these status
        for all - All
        for Pending - Pending
        for Active - Active
        for Paused - Paused
        for Expired - Expired
        '''
        sleep(8)
        button=driver.find_element(By.XPATH, "//button[@id='btn-tenantDash-filter"+filterType+"']")
        if button.tag_name == 'button':
            button.click()
            print('Is ',button.text,'Button Enabled: ',button.is_enabled())
            print('Is ',button.text,'Button Displayed: ',button.is_displayed())
            print('Clicked button has status: ',button.text)
            print()
            sleep(2)
        else:
            print('Element is not button type for filtering campaign')
    
    def searchCampaign(self):
        sleep(10)
        element=driver.find_element(By.ID, 'inp-tenantDash-searchCampaign')
        placeholder=element.get_attribute('placeholder')
        print(element.tag_name)
        if placeholder == 'Search Campaigns':
            element.click() and element.clear()
            element.send_keys('test')
        else:
            print('It is not search campaign element!')
        rows=driver.find_elements(By.CLASS_NAME, "xad-table-row ng-scope")
        print('lenth of total rows in table: ',len(rows))
        if len(rows) == 0:
            print('There are no campaigns that match the selected filters.')
        else:
            print('Campaigns that match the selection filters are listed below.')

    def ColumnPicker(self,columnSelection,action):
        '''
        columnSelection type = Dimension, Delivery, Flight and budget, Total sec. actions, Visits
        action is for Apply/Cancel button
        '''
        sleep(20)
        picker=driver.find_element(By.ID, "btn-cm-columnPicker")
        if picker.tag_name == 'button':
            picker.click()
            sleep(5)
            heading=driver.find_element(By.XPATH, "//div[contains(text(),'Customize Columns')]")
            print('#'*50)
            print('Column Picker Model Details')
            print(heading.text)    


            presets=driver.find_element(By.XPATH, "//h5[contains(text(),'Available Presets')]")
            buttons=driver.find_elements(By.XPATH, "//div[@ng-click='vm.selectPreset(presetName)']")
            print('*'*50)
            print(presets.text)
            print('Total Available Presets are: ',len(buttons))
            print()
            for button in buttons:
                button.click()
                print('Pressed button is ',button.text)
                sleep(1)
            selection=driver.find_element(By.XPATH, "//div[@class='section-title ng-binding'][contains(text(),'"+columnSelection+"')]")
            selection.click()


            section=driver.find_element(By.XPATH, "//h5[contains(text(),'Sections')]")
            print('*'*50)
            print(section.text)
            print()
            checkboxes=driver.find_elements(By.NAME, "selectedHeaders[]")
            check_text=driver.find_elements(By.XPATH, "//div[@class='section-item ng-scope']/label[@class='ng-binding']")
            print('Count of checkboxes labels ',len(check_text))
            print('Count of checkboxes available under',section.text,len(checkboxes))
            print()
            for chktext in check_text:
                print(chktext.text)


            selection=driver.find_element(By.XPATH,"//h5[contains(text(),'Selected Columns')]")
            print('*'*50)
            print(selection.text)
            print()
            elements=driver.find_elements(By.XPATH, "//div[@class='selected-item ng-binding ng-scope']")
            print('Element selected in ',selection.text,':',len(elements))
            print()
            for element in elements:
                print(element.text)
        else:
            print('Element is not button unable to click')

        if action == 'Apply':
            driver.find_element(By.XPATH, "//div[@class='footer-buttons']//button[contains(text(),'"+action+"')]").click() #Apply
            print("Apply button pressed on Column picker model")
        else:
            driver.find_element(By.XPATH, "//span[contains(text(),'×')]").click()
            print("Cancel button pressed on Column picker model")

    def ExportCampaignData(self):
        sleep(5)
        print("*"*50)
        export = driver.find_element(By.ID, 'btn-cm-exportData')
        if export.is_enabled() == False:
            print('Export button is disabled')
            
        else:
            print('Export button is enabled!!')

        global_checkbox=driver.find_element(By.XPATH, "//input[@ng-change='globalCheckboxChanged(item)']")
        if global_checkbox.tag_name == 'input' and global_checkbox.is_enabled() == True:
            global_checkbox.click()
            print('Clicked on global checkbox')
            export.click()
            print('Downloaded the campaigns data')
            print()
    
        selectionCount = driver.find_element(By.XPATH, "//strong[@class='ng-binding']")
        print('Selct all campaign Count:',selectionCount.text) 

        rows=driver.find_elements(By.XPATH, "//div[contains(@id, 'tableBody-row')]") 
        print('Total rows available in the table except Xad header: ',len(rows))
        print()
        linksInXadTableRow=driver.find_elements(By.XPATH, "//a[@class='ng-scope']") #//a[@class='ng-scope']
        tableHeaderColumnSar=driver.find_elements(By.XPATH, "//span[@ng-if='!item.sortable']")
        print("*"*50)
        print('Count of links in Xad Table Row:',len(linksInXadTableRow))
        for link in linksInXadTableRow:
            # link.click()
            print('Link name is:',link.text)
        print("*"*50)
        print('Count of Non links in Xad Table Row:',len(tableHeaderColumnSar))
        for header in tableHeaderColumnSar:
            print('Non-link Column name is:',header.text)
        
    def pagination(self):
        print('*' * 50)
        sleep(10)
        buttons=driver.find_elements(By.XPATH, "//ul[@max-size='5']/li/a")
        f = 'First'
        l = 'Last'
        next_button='›'
        previous_button='‹'

        paginationLinkCount=len(buttons) + 1
        print('Total button are:',paginationLinkCount)
        if f == buttons[0].text and l == buttons[-1].text and next_button == buttons[-2].text and previous_button == buttons[1].text:
            print('First,<,> and Last button names are matching successfully!!!')
        print('Buttons used in pagination are listed below:')
        print('#'*10)
        for a in buttons:
            print(a.text)
        print('#'*10)
        first = driver.find_element(By.XPATH, "//a[contains(text(),'First')]")
        previous = driver.find_element(By.XPATH,"//a[contains(text(),'‹')]")
        if first.is_enabled() == True and previous.is_enabled() == True:
            print('Button(First) and Previous (<) are disabled by default')
        else:
            print('By Default no buttons are disabled under pagination!!')

        element=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='pagination-select']/select[@ng-change='vm.updateItemsPerPage()']")))
        select=Select(element)

        print('No of options available in dropdown per page:',len(select.options))
        for option in select.options:
            print('Options are:',option.text)


        if int(select.first_selected_option.text) == 10:
            print('Test Passed, By default selection is 10!!')
        else:
            print('Test Failed, Default selection values in incorrect')
        select.select_by_value("number:25")
        print('Value selected is:25')


t=TenantDashboard()
t.SelectOrg('3.15')#DelCastillo
t.searchbox() #not working while executing all

# t.ColumnPicker('Flight and budget')
# t.ColumnPicker('Total sec. actions')
# t.ColumnPicker('Visits')
# t.hamburger()
# t.links_Buttons() 
# t.SelectTenant('#DelCastillo') #DelCastillo,DelCastillo,Del Castillo Agency
# t.SelectOrg('3.15')#DelCastillo
# t.SelectAccount('Del Castillo Agency')
# t.SelectTenant('#GatewayFantasticSams')
# t.SelectOrg('GatewayFantasticSams')
# t.SelectAccount('Fantastic Sams Brea')
# t.TenantTitleSection()
# # t.searchbox() #not working while executing all
# # t.TermAndPrivacyPolicy() #not working while executing all
# t.LiveToDate('2020-06-30','2020-10-29','applyBtn','success') 
# t.LiveToDate('2020-08-30','2020-12-29','cancelBtn','default')
# t.campaignStatusFilter('Pending')
# t.campaignStatusFilter('Active')
# t.campaignStatusFilter('Paused')
# t.campaignStatusFilter('Expired')
# t.campaignStatusFilter('All')
# t.searchCampaign()
# t.ColumnPicker('Delivery','Apply') #1st argument(Dimension, Delivery, Flight and budget, Total sec. actions, Visits) is to click on section and 2nd argument(Apply/Cancel) is for Apply/Cancel button
# t.SelectOrg('3.15')
# t.ExportCampaignData()  
# t.pagination()  
sleep(10)
driver.quit()
