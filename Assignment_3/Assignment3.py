#Test case
#1) open the web browser chrome
#2)Open URL https://www.netflix.com/ca/login
#3)Enter the USERNAME (gagandkaur1994@gmail.com)
#4)Enter the password (gagan283)
#5)Click on Signin
#6)Go To the Next following page of Netflix
#7)Close the browser





#Import the required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user_name = "gagandkaur1994@gmail.com"
password = "gagan283"

# set the driver over here
driver = webdriver.Chrome()

#Navigating the website of netflix
driver.get("https://www.netflix.com/ca/login")


# Fill up the username and password

element = driver.find_element("id","id_userLoginId")
element.send_keys(user_name)
element = driver.find_element("id","id_password")
element.send_keys(password)


#Click on the following page of netflix
element.send_keys(Keys.RETURN)
time.sleep(4)
element = driver.find_element("id","button--nmhp-card-faq-accordion--0")
element.send_keys(Keys.RETURN)
time.sleep(4)

# Close the driver
driver.close()