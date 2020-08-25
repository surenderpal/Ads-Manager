from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://www.amazon.in/')

cookies=driver.get_cookies() # capture all cookies created by browser
print(len(cookies)) #print number of cookies have been created
print(cookies) #print all the cookies pair

#Addinng new cookie to the browser
cookie={'name':'Mycookie','value':'123456789'}
driver.add_cookie(cookie)

cookies=driver.get_cookies() # capture all cookies created by browser
print(len(cookies)) #print number of cookies have been created
print(cookies) #print all the cookies pair

driver.delete_cookie('Mycookie') #Deleting selected cookies

cookies=driver.get_cookies() # capture all cookies created by browser
print(len(cookies)) #print number of cookies have been created
print(cookies) #print all the cookies pair

cookies=driver.delete_all_cookies() #deleting all cookies
print(cookies) #print all the cookies pair