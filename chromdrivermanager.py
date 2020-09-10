from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #for chrome
# driver=webdriver.Chrome(ChromeDriverManager().install()) #for chrome
from webdriver_manager.firefox import GeckoDriverManager #for firefox
# driver=webdriver.Firefox(executable_path=GeckoDriverManager().install()) #for firefox
from webdriver_manager.microsoft import IEDriverManager #for Ie
# driver=webdriver.Ie(IEDriverManager().install()) #for Ie
from webdriver_manager.microsoft import EdgeChromiumDriverManager #with Edge
# driver=webdriver.Edge(EdgeChromiumDriverManager().install()) #with Edgedriver 
import time

browserName = 'firefox'
if browserName =='chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install()) #for chrome 
elif browserName == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) #for firefox
elif browserName == 'safari':
    driver =  webdriver.Safari()
else:
    print('Please pass the correct browser nanme:' + browserName)
    raise Exception('Driver is not found!')

driver.get('https://app.hubspot.com/login')
driver.maximize_window()
time.sleep(7)
driver.find_element_by_id('username').send_keys('surender@gmail.com')
driver.find_element_by_id('password').send_keys('surender')
driver.find_element_by_id('checkbox-content-4').click()
driver.find_element_by_id('loginBtn').click()
print(driver.title)
driver.quit()