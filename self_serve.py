from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("http://ads-release-3-13-np.groundtruth.com/")
email=driver.find_element_by_xpath('//*[@id="inp-signin-usernameLogin"]')
email.send_keys('gt.surender@protonmail.com')
pwd=driver.find_element_by_xpath('//*[@id="inp-signin-passwordLogin"]')
pwd.send_keys('Groundtruth@9')
signInButton=driver.find_element_by_xpath('//*[@id="btn-signin-signIn"]').click()
time.sleep(3)
# ---clicking on hamburger menu----
hamburger = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".app-screen #btn-appMenu")))
hamburger.click()
# ------clicking on Menu Dashboard
# view_Dashboard = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-dashboard")))
# view_Dashboard.click()

# ----selecting  Organization from hamburger------
# org = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-org")))
# org.click()

# ----selecting  Manage Accounts from hamburger------
# manage_accounts = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-manageAccounts")))
# manage_accounts.click()

# ----selecting  Billing from hamburger------
# billing = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-billing")))
# billing.click()

# ----selecting  Manage Users from hamburger------
# manage_users = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-manageUsers")))
# manage_users.click()


# ----selecting  Report Scheduler from hamburger------
# reportScheduler = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-reportScheduler")))
# reportScheduler.click()


# ----selecting  profile from hamburger------
# profile = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-profile")))
# profile.click()


# ----selecting  Account Setting from hamburger------
# acc_setting = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-accountSettings")))
# acc_setting.click()

# ----selecting  Help from hamburger------
# help = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-help")))
# help.click()

# ----selecting  sign out from hamburger------
# logout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".app-screen #btn-appMenu-signOut")))
# logout.click()

time.sleep(5)
driver.close()
