from selenium import webdriver
import time
class Login():
    """ Ads manager login class"""
    # staic variable
    driver=webdriver.Chrome()
    driver.get("http://ads-release-3-12-np.groundtruth.com/")
    
    def login_ads(self,username,password):
        email=self.driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
        email.send_keys(username)
        pwd=self.driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
        pwd.send_keys(password)
        signInButton=self.driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]')
        signInButton.click()
        print("{} has been logged in successfully!!".format(username))