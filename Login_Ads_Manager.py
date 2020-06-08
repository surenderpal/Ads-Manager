from selenium import webdriver
import time
import selenium
driver=webdriver.Chrome()
driver.get("http://ads-release-3-12-np.groundtruth.com/")
time.sleep(5)
email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
email.send_keys('surender.pal@groundtruth.com')
pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
pwd.send_keys('Surenderpal@1991')

signInButton=driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]')
signInButton.click()


searchTenant=driver.find_element_by_xpath('//*[@id="tenantMultiselect"]/div/div/div[1]/span[2]')
searchTenant.send_keys('Molio Inc')
time.sleep(5)
searchOrg=driver.find_element_by_xpath('//*[@id="organizationMultiSelect"]/div/div/div[1]/span[2]')
searchOrg.send_keys('Molio Inc')
time.sleep(5)
searhAccounts=driver.find_element_by_xpath('//*[@id="accountsMultiselect"]/div/div/div[1]/span[2]')
searhAccounts.send_keys('Alba Botanica')
time.sleep(5)

usrOption=driver.find_element_by_xpath('//*[@id="btn-userOptions-userOptionsMenuToggle"]/span')
logout=driver.find_element_by_xpath('/html/body/ui-view/div/div[1]/user-options/div/ul/li[4]/a')
logout.click()
