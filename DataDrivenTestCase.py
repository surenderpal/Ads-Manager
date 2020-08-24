import XLUtils
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://demo.guru99.com/test/newtours/index.php")
driver.maximize_window()
time.sleep(1)

path="/Users/surenderpal/Downloads/Login.xlsx"
rows=XLUtils.getRowCounnt(path,'NewTours')
for r in range(2,rows+1):
    time.sleep(3)
    username=XLUtils.readData(path,'NewTours',r,1)
    password=XLUtils.readData(path,'NewTours',r,2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("submit").click()

    print(driver.title)

    if driver.title=="Login: Mercury Tours":
        print('test is passed')
        XLUtils.writeData(path,'NewTours',r,3,'test passed')
    else:
        print('test is failed')
        XLUtils.writeData(path,'NewTours',r,3,"test failed")
        
    driver.find_element_by_link_text("Home").click()    
    time.sleep(2)
driver.close()
       