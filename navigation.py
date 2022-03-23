from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# PATH = "C:\Program Files (x86)\chromedriver.exe"
PATH = Service(ChromeDriverManager().install())
driver  = webdriver.Chrome(service=PATH)

driver.get("https://www.techwithtim.net/")


link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()


    # back to previous page
    driver.back()

    # next page
    driver.forward()
    
except Exception as e:
    print(e)
    driver.quit()
