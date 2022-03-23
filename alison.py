import time
import csv,io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
# PATH = Service(ChromeDriverManager().install())
# driver  = webdriver.Chrome(service=PATH)
driver  = webdriver.Chrome(PATH)

msExcel = 'Microsoft Excel 2013 - Intermediate Course'
msPPT ='Microsoft PowerPoint 2013 for Beginners - Create Amazing Presentations'
msWord = 'Diploma in Microsoft Word 2013 Intermediate'

currentUrl = driver.current_url
siteUrl = "https://alison.com/"
dashboardUrl = "https://alison.com/dashboard/"

password1 = "Its101$1"
password2 = "ITS101$1"
password3 = "Its10141"
password4 = "Its10141"

# emai_l = "jasperkekeli2000@gmail.com"
error_msg = "These credentials do not match our records."


csv_file = open('files.csv')
data_set = csv_file.read()
io_string = io.StringIO(data_set)
next(io_string)
for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    scores = []
    coaurTitle = []
    
    driver.implicitly_wait(10)
    driver.get("https://alison.com/login")
    driver.implicitly_wait(10)

    # set user email
    emai_l = column[2]

    try:
        email = driver.find_element(By.NAME, 'email')
        password = driver.find_element(By.NAME, 'password')

        email.clear()
        email.send_keys(emai_l)

        password.clear()
        password.send_keys(password1)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "submit-login"))
        )
        element.click()

        driver.implicitly_wait(10)
        if driver.current_url == siteUrl:
            # click on the profile icon
            driver.get(dashboardUrl)

        elif driver.current_url == dashboardUrl: 
            print("hamza baba")
        else:      
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "alison_logo"))
            )
            element.click()

    
        
        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "widget__row-item"))
        # )
        driver.implicitly_wait(10)
        articles = driver.find_elements(By.CLASS_NAME, "widget__row-item")
        for article in articles:
            driver.implicitly_wait(10)
            header = article.find_element(By.CLASS_NAME, "widget__course-title")
            driver.implicitly_wait(10)
            coaurTitle.append(header.text)
            driver.implicitly_wait(10)
            score = article.find_element(By.CLASS_NAME, "widget__score")
            driver.implicitly_wait(10)
            scores.append(score.text)
                
        driver.implicitly_wait(10)
        print(coaurTitle)
        print(scores)

        driver.implicitly_wait(10)
        # logout 
        driver.get("https://alison.com/logout/")

        driver.implicitly_wait(10)

    except Exception as e:
        print(e)
        driver.quit()

time.sleep(10)