import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import click

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(3)

######### RADIO BUTTON

driver.find_element(By.XPATH,"//input[@value='radio1']").click()
driver.find_element(By.XPATH,"//input[@value='radio3']").click()
driver.find_element(By.XPATH,"//input[@value='radio2']").click()