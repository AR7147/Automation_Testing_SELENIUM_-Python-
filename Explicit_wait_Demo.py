import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Explicit_Wait_DEMO():
     def expilicit_wait(self):
        driver = webdriver.Chrome()
        ##### implicity will check for the web elements on the page
        driver.get("https://login.salesforce.com/?locale=eu")