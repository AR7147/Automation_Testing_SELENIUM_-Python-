import driver
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/locatorspractice/")
driver.maximize_window()
time.sleep(3)

# Email field
driver.find_element(By.ID,"inputUsername").send_keys("Rahul")

# passwd Field
driver.find_element(By.NAME,"inputPassword").send_keys("hithere")

#forget passwd
driver.find_element(By.LINK_TEXT,"Forgot your password?").click()


########################### AFTER THE PASSWORD RESET FORM
#NAME EMAIL PHONE-NUMBER
#driver.find_element(By.CLASS_NAME,"infoMsg").send_keys("@Abcd1234")
#driver.find_element(By.CLASS_NAME,"infoMsg").send_keys("@Abcd1234")
#driver.find_element(By.CLASS_NAME,"infoMsg").send_keys("@Abcd1234")

driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Rahul")
driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("rahul@example.com")
driver.find_element(By.XPATH, "//input[@placeholder='Phone Number']").send_keys("1234567890")

#driver.find_element(By.XPATH,"//input[@placeholder='Name']").send_keys()


#driver.find_element(By.CLASS_NAME,"reset-pwd-btn").click()

# Click on Reset Password button
driver.find_element(By.CLASS_NAME, "reset-pwd-btn").click()

# Get the password reset message
message = driver.find_element(By.CLASS_NAME, "infoMsg").text
print("Reset Message:", message)

