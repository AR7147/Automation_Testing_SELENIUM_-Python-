#import EC

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # ✅ Correct


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/locatorspractice/")
driver.maximize_window()
time.sleep(4)


# //tagname[@attribute=""] -> //input[@type='submit']

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("HElloTHERE")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(12345678)


#driver.find_element(By.XPATH,"//input[@type='checkbox']")

driver.find_element(By.NAME,"chkboxOne").click()
driver.find_element(By.NAME,"chkboxTwo").click()


### SUBMIT
driver.find_element(By.XPATH,"//button[@type='submit']").click()



#### IT WILL WAIT TILL THE ERROR MESSAGE POPUP's
Message1 = (WebDriverWait(driver, 10).until
           (EC.visibility_of_element_located((By.XPATH, "//p[@class='error']"))).text)
#print("Error Message:", Message1)
print(Message1)

#WebDriverWait(driver,25).until(EC.visibility_of_element_located((By.XPATH)))
# ,"//input[@placeholder='Phone Number']").send_keys(123)

#driver.find_element(By.CLASS_NAME,'forgot-pwd-container').click()
driver.find_element(By.LINK_TEXT,"Forgot your password?").click()

### NEXT SCREEN INFO FILL

driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Rahul")
driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("rahul@example.com")
driver.find_element(By.XPATH, "//input[@placeholder='Phone Number']").send_keys(8784516)


driver.find_element(By.CLASS_NAME, "reset-pwd-btn").click()

# Get the password reset message
message = driver.find_element(By.CLASS_NAME, "infoMsg").text
print("Reset Message:", message)

# HOLD THE WINDOW
time.sleep(5)
#driver.quit()
driver.implicitly_wait(10)