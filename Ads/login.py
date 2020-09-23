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
    def searchbox(self):
        searchBox=driver.find_element(By.ID, "inp-base-searchbox-new")
        searchBox.click()
        searchBox.send_keys('test',Keys.ENTER)
        # driver.back()

        driver.find_elements(By.XPATH, "")
        # if driver.find_element(By.ID, "inp-search-dateCreated-all").get_attribute('type') =='radio':

        #     print('element is radio button and ')
        #     driver.find_element(By.ID, "inp-search-dateCreated-all").is_selected():
        #     driver.find_element(By.ID, "inp-search-dateCreated-all").get_attribute('')
        #     print('Default value selected is: ',)
        # driver.find_element(By.ID, "//input[@id='inp-search-dateCreated-week']").click()
        



    def pagination(self):
        wait=WebDriverWait(driver, 40)
        element=Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@class='ng-pristine ng-valid ng-not-empty ng-touched']"))))
        select=Select(element)
        select.select_by_visible_text('10')
        sleep(2)
        select.select_by_visible_text('25')
        sleep(2)
        select.select_by_visible_text('50')
        sleep(2)
        print('Total options available for the selection: ',len(select.options)) #print count of options
        all_options=select.options
        for option in all_options:
            print(option.text)

t=TenantDashboard()
t.hamburger()
# # t.links_Buttons()
# t.SelectTenant('#DelCastillo')
# t.SelectOrg('DelCastillo')
# t.SelectAccount('Del Castillo Agency')
# t.SelectTenant('#GatewayFantasticSams')
# t.SelectOrg('GatewayFantasticSams')
# t.SelectAccount('Fantastic Sams Brea')
t.searchbox()
t.pagination()