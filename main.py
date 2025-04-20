from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def Browser():
    chromedriver = webdriver.Chrome()
#TARGET_WEBSITE
    chromedriver.get("https://www.google.co.uk/")
    print("Chrome Launched")

# making method for text_Box

def selenium_TexTBox(fire_driver):
    fire_driver = webdriver.Firefox()
    fire_driver.get('https://www.google.co.uk/')
    first_name = fire_driver.find_element(By.NAME, "N")
    first_name.send_keys("Selenium in python an easy guide for beginners ")
    first_name.send_keys(Keys.RETURN)


















##CAlling the browser function
    if __name__ == '__main__':
     Browser()
     selenium_TexTBox()


