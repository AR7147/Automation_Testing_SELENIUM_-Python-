from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
## Target specific element on the page

# ID,  Xpath, CSS selector, Class_name, name, Link_text
# Goal is to find the element



#driver.find_element(By.CLASS_NAME,"form_group").send_keys("abdulrafay2564@gmail.com")

############################## FOR_THE_PASSWORD #######################################
#By using name
#driver.find_element(By.NAME,"password").send_keys("HackerArise")



# By using XPATH
    # //tagname[@attribute=""] -> //input[@type='submit']
#driver.find_element(By.XPATH,"//input[@type='submit']").click()
#message = driver.find_element(By.CLASS_NAME,"error-message-container").text
#print(message)

#driver.find_element(By.XPATH,"")


# By using LINK_TEXT
#driver.find_element(By.LINK_TEXT)

# By using CLASS_NAME
#driver.find_element(By.CLASS_NAME,"form_group").send_keys("123")

#Click on the login button as well ############################################# { M A I N }


## WRONG RIGHT CREDIENTIALS
# FOR_THE_EMAIL
# driver.find_element(By.NAME,"user-name").send_keys("abdulrafay2564@gmail.com")
driver.find_element(By.ID, "user-name").send_keys("abdulrafay2564@gmail.com")
#FOR PASSWORD & By using ID
driver.find_element(By.ID,"password").send_keys("786","123")
# Click button
##driver.find_element(By.ID,"login-button").click()

# X-PATH
# Submit
# driver.find_element(By.XPATH,"//input[@type='submit']").click()

# for class value we use "HASH"
driver.find_element(by=By.CSS_SELECTOR,value="#login-button").click()
#driver.find_element(By.CSS_SELECTOR,"input[name='login-button']")
#driver.find_element(By.CSS_SELECTOR,"login-button").click()
error_message = driver.find_element(By.CLASS_NAME,"error-message-container").text
print(error_message)
# to verify that the following keyword is present in the message
assert "service" in error_message;print("Test case works")

## RIGHT CREDIENTIALS
#driver.find_element(By.ID, "user-name").send_keys("standard_user")
#FOR PASSWORD & By using ID
#driver.find_element(By.ID,"password").send_keys("secret_sauce")
# Click button
#driver.find_element(By.ID,"login-button").click()

# Submit
#driver.find_element(By.XPATH,"//input[@type='submit']")
#error_message = driver.find_element(By.CLASS_NAME,"error-message-container").text
#print("LOGIN _ SUCESSFULL")



