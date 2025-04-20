from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # ✅ Correct Import

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# Create WebDriverWait instance
Wait = WebDriverWait(driver, 10)


print("\nTest cases ready to launch......... \n")
################################################################################
################### FINAL TEST CASES FOR "practiceAutomationtesting.com"
################################################################################

# ========================= Test Case 1: Negative Login (Incorrect Username) =========================
driver.find_element(By.XPATH, "//input[@id='username']").clear()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("incorrectUser")

driver.find_element(By.XPATH, "//input[@id='password']").clear()
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Password123")

driver.find_element(By.XPATH, "//button[@id='submit']").click()

# Wait for error message
Peak = Wait.until(EC.presence_of_element_located((By.ID, "error"))).text
print(Peak, "\nmessage working successfully\n")

time.sleep(2)

# ========================= Test Case 2: Negative Login (Incorrect Password) =========================
driver.find_element(By.XPATH, "//input[@id='username']").clear()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("student")

driver.find_element(By.XPATH, "//input[@id='password']").clear()
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("wrongpassword")

driver.find_element(By.XPATH, "//button[@id='submit']").click()

# Wait for error message
Push = Wait.until(EC.presence_of_element_located((By.ID, "error"))).text
print(Push, "\nmessage working successfully\n")

time.sleep(2)

# ========================= Test Case 3: Positive Login Test =========================
driver.find_element(By.XPATH, "//input[@id='username']").clear()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("student")

driver.find_element(By.XPATH, "//input[@id='password']").clear()
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Password123")

driver.find_element(By.XPATH, "//button[@id='submit']").click()

# Wait for success message
Pop = Wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text  # ✅ Update selector
print(Pop, "\nLogin successful\n")

# ========================= Logout =========================
logout_button = Wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wp-block-button")))
logout_button.click()
print("\nLogout Successful\n")

time.sleep(2)

print("\nALL TEST CASES EXECUTED SUCCESSFULLY!\n")

driver.quit()