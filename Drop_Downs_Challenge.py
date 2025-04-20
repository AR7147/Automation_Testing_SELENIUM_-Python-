import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.automationtesting.co.uk/dropdown.html#")
driver.maximize_window()

Menu1 = Select(driver.find_element(By.XPATH,"//a[normalize-space()='Animals']"))
Menu1.select_by_visible_text()
Menu1.select_by_index()

#Drop_Down_Menu = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
