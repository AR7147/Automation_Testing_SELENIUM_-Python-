import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://qa-automation-practice.netlify.app/alerts")

#time.sleep(3)

driver.find_element(By.CLASS_NAME,"btn-primary").click()

time.sleep(3)

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

# ASSERT TO CHECK TEST IN PASS OR FAIL
def true():
    assert "an" in alertText
    alert.accept()

print(true())