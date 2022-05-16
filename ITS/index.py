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


# print(driver.title)

search = driver.find_element(By.NAME, 's')
search.send_keys("test")
search.send_keys(Keys.RETURN)

# wait for target hits
try:
    
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # 
    articles = main.find_elements(By.TAG_NAME, "article")
    print(type(articles))
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-header")
        print(header.text)

except Exception as e:
    print(e)
    driver.quit()
# print(driver.page_source)


