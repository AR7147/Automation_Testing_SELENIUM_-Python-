from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

print("\nWEB-DRIVER-LAUNCHED")


## Static Drop Down
# DropDown is the object of select class

driver.find_element(By.XPATH,"//input[@name='email']").clear()
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("TYPING THE MALE")

Drop_Down_Menu = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# Selecting Male
Drop_Down_Menu.select_by_index(0)
Drop_Down_Menu.select_by_visible_text("Male")

time.sleep(4)

# Female
driver.find_element(By.XPATH,"//input[@name='email']").clear()
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("TYPING THE Female")
Drop_Down_Menu2 = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# Selecting Female
Drop_Down_Menu2.select_by_index(1)
Drop_Down_Menu2.select_by_visible_text("Female")


time.sleep(5)

driver.quit()