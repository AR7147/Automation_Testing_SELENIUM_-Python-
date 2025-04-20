import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://qa-automation-practice.netlify.app/radiobuttons.html")

Button_1 = driver.find_element(By.ID,"radio-button1").click()

time.sleep(2)

Button2 = driver.find_element(By.ID,"radio-button2").click()

time.sleep(2)

Button3 = driver.find_element(By.ID,"radio-button3").click()

