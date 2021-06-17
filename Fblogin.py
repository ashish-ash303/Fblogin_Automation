from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)


driver.get('https://www.facebook.com/')
time.sleep(2)
userid = driver.find_element_by_xpath('//*[@id="email"]')
print('found userid')
time.sleep(2)
password = driver.find_element_by_xpath('//*[@id="pass"]')
print('found pssword')
time.sleep(4)
login = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')


print('login')
time.sleep(2)
userid.send_keys("email")
print('Entered userid1')
time.sleep(2)
password.send_keys('Password')
print('Entered pss')
time.sleep(2)
login.click()
print('logged in ')
