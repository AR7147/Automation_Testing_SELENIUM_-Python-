import time

import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

time.sleep(3)

print("\nWeb driver launched")

#driver.find_element(By.CSS_SELECTOR,"#autosuggest")
#driver.find_element(By.ID,"autosuggest").send_keys("ind")
#time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#autosuggest")
driver.find_element(By.ID,"autosuggest").send_keys("pa")
time.sleep(2)

Countries1 = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(Countries1))

#Countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
#print(len(Countries))

for country in Countries1:
    if country.text == "Pakistan":
        country.click()
        break

#print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

## Assert to check whether test case pass or fail

assert driver.find_elements(By.ID,"autosuggest").get_attribute("value") == "Pakistan"


########################################################################333
# Interview question
#Q: When update value danamically using script how do you extraxt text ?
#Q: We use get_attribute
