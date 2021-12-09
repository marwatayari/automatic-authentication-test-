from selenium import webdriver
import time
Username= 'Admin'
Password= 'admin123'

driver = webdriver.Chrome("C:\\Users\\HP\\PycharmProjects\\pythonProject\\drivers\\chromedriver.exe")
driver.get('https://opensource-demo.orangehrmlive.com/')
print("driver.title")  #return the title of the page
print("driver.current_url")  #return url of the page
user_input = driver.find_element_by_id('txtUsername')
user_input.send_keys( Username )

password_input = driver.find_element_by_id('txtPassword')
password_input.send_keys(Password)

login_button = driver.find_element_by_id('btnLogin')
login_button.click()
time.sleep(5)
driver.close()