import click
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://qa-automation-practice.netlify.app/checkboxes")


Check1 = driver.find_element(By.ID,"checkbox1").click();
time.sleep(2)

Check2 = driver.find_element(By.ID,"checkbox2").click();
time.sleep(2)

Check3 = driver.find_element(By.ID,"checkbox3").click();
time.sleep(1)

driver.find_element(By.CLASS_NAME,"btn").click()

