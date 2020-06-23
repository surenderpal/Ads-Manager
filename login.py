from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://ads-release-3-12-np.groundtruth.com/")
time.sleep(5)
email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
email.send_keys('surender.pal@groundtruth.com')
pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
pwd.send_keys('Surenderpal@1991')

signInButton=driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]')
signInButton.click()


TenantDD=driver.find_element_by_xpath(".//span[@class='dropdown-title ng-binding']").click()
TenantSB=driver.find_element_by_xpath(".//input[@id='search-dropdown-list-Tenant']")
TenantCkbox=driver.find_element_by_xpath(".//input[@name='Tenant-2']")
driver.close()
