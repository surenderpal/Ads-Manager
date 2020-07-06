from selenium import webdriver
import time
class Ads_Manage_Login():
    """ Ads manager login class"""
    # staic variable
    driver=webdriver.Chrome()
    driver.get("http://ads-release-3-12-np.groundtruth.com/")
    
    def __init__(self,username,password): #constructor defined for dynamic username and password
        self.username=username
        self.password=password
    
    def login_ads(self):
        email=self.driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
        email.send_keys(self.username)
        pwd=self.driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
        pwd.send_keys(self.password)
        signInButton=self.driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]')
        signInButton.click()
        print("{} has been logged in successfully!!".format(self.username))
l=Ads_Manage_Login('surender.pal@groundtruth.com','Surenderpal@1991')
l.login_ads()
