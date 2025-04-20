import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(3)

#CheckBox 1
#driver.find_element(By.ID,"checkBoxOption1").click()
#time.sleep(1)

#CheckBox 2
#driver.find_element(By.ID,"checkBoxOption2").click()
#time.sleep(1)

#CheckBox 3
#driver.find_element(By.ID,"checkBoxOption3").click()
#time.sleep(1)

# Again click that will un select the checkboxes
#driver.find_element(By.ID,"checkBoxOption3").click()
#driver.find_element(By.ID,"checkBoxOption2").click()
#driver.find_element(By.ID,"checkBoxOption1").click()


#time.sleep(2)

# IT will select all checkboxes using loop
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()


