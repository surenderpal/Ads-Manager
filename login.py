from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("http://ads-release-3-12-np.groundtruth.com/")
time.sleep(5)
email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
email.send_keys('surender.pal@groundtruth.com')
pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
pwd.send_keys('Surenderpal@1991')

signInButton=driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]')
signInButton.click()

# ---clicking on hamburger menu----
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu")))
button.click()
time.sleep(5)
driver.close()
