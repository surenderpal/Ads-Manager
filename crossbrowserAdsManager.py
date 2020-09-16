from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #for chrome
from webdriver_manager.firefox import GeckoDriverManager #for firefox
from webdriver_manager.microsoft import IEDriverManager #for IE
from webdriver_manager.microsoft import EdgeChromiumDriverManager #for edge
from time import sleep

# def browserName(bname):#bname
bname='chrome'
if bname=='chrome':
    driver=webdriver.Chrome(ChromeDriverManager().install()) #this will install latest chrome driver manager
elif bname=='firefox':
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install()) #it will install latest firefox driver manager
elif bname=='ie':
    driver=webdriver.Ie(IEDriverManager().install())
elif bname=='edge':
    driver=webdriver.Edge(EdgeChromiumDriverManager().install())
elif bname=='safari':
    driver=webdriver.Safari()
else:
    print('Please pass the correct browser name' + bname)
driver.get('https://ads-release-3-14-np.groundtruth.com/')
# browserName('firefox')


# login class to automate the login process
class login():
    driver.maximize_window()
    def AdManager(self,username,password):
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_id('btn-signin-signIn').click()
l=login()
l.AdManager('surender.pal@groundtruth.com','Surenderpal@1991')