from selenium import webdriver
import time
class signup:
    driver=webdriver.Chrome()
    driver.get("http://ads-release-3-13-np.groundtruth.com/")
    time.sleep(5)
    signup=driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/span/a').click()
    f_name=driver.find_element_by_name('first_name')
    f_name.send_keys('test')
    l_name=driver.find_element_by_name('last_name')
    l_name.send_keys('demo')
    ttl=driver.find_element_by_name('title')
    ttl.send_keys('Tester@GroudTRuth')
    phn=driver.find_element_by_name('phone_number')
    phn.send_keys('09876543214')
    orgname=driver.find_element_by_name('organizationName')
    orgname.send_keys('surender Inc.')
    email=driver.find_element_by_name('username')
    email.send_keys('suren@surender.com')
    pwd=driver.find_element_by_name('password-signup')
    pwd.send_keys('Test@1234')
    repwd=driver.find_element_by_name('password-repeat-signup')
    repwd.send_keys('Test@1234')
    if driver.find_element_by_id("inp-signin-signupTermsCheckbox").get_attribute("type") == "checkbox":
        print("Element is a checkbox")
    else:
        print("Element is not a checkbox")
    cond=driver.find_element_by_id("inp-signin-signupTermsCheckbox").click()
    sbmt=driver.find_element_by_id("btn-signin-signUpConfirm").click()
    time.sleep(5)
    driver.save_screenshot('successfully_registered_screenshot.png')
    driver.close()
s=signup()
# https://ads-release-3-13-np.groundtruth.com/login?subsession=924ba0de-a7fc-4d11-b615-cd074c5eafb2&returnUrl=%2F
# https://ads-release-3-13-np.groundtruth.com/login?subsession=a6f7189a-0dca-4462-9242-75c9f4b9ad59&returnUrl=%2F