from time import sleep
from selenium import webdriver

browser = webdriver.Firefox(executable_path='../Driver/geckodriver')
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')
sleep(5)


#enter user name
username_input = browser.find_element_by_css_selector("input[name='username']")
username_input.send_keys("enter user name")

#enter password
password_input = browser.find_element_by_css_selector("input[name='password']")
password_input.send_keys("enter password")


#To subi=mit and login into insta
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.submit()

sleep(5)
notnow_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
notnow_button.click()
sleep(5)

browser.close()
