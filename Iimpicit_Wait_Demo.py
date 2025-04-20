import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demoimplicit_Wait():
     def impicit_wait(self):
        driver = webdriver.Chrome()
        ##### implicity will check for the web elements on the page
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=eu")
        driver.find_element(By.ID,"username").send_keys("REX")
        driver.quit()

### Creating objet of the class
## implicit which holds the reference of the object of the class

implicit = Demoimplicit_Wait()
implicit.impicit_wait()


