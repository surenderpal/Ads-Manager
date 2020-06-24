from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("http://ads-release-3-13-np.groundtruth.com/")
email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
email.send_keys('surender.pal@groundtruth.com')
pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
pwd.send_keys('Surenderpal@1991')
signInButton=driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]').click()
time.sleep(3)
# ---clicking on hamburger menu----
hamburger = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu")))
hamburger.click()

# ------clicking on Tenant Dashboard
# tenant_dashboard = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-tenant-dashboard")))
# tenant_dashboard.click()

# ----selecting  Manage Organization from hamburger------
# org = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-manageOrg")))
# org.click()

# ----selecting  Manage Users from hamburger------
# manage_accounts = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-manageUsers")))
# manage_accounts.click()


# ----selecting  creative Repo from hamburger------
# creative_repo = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-creativeRepo")))
# creative_repo.click()

# ----selecting  reports from hamburger------
# reports = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-reportScheduler")))
# reports.click()

# ----selecting  profile from hamburger------
# profile = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-profile")))
# profile.click()

# ----selecting  Help from hamburger------
# help = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-help")))
# help.click()

# ----selecting  sign out from hamburger------
logout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-signOut")))
logout.click()

time.sleep(5)
driver.close()
