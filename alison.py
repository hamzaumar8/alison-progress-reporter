from operator import index
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
driver  = webdriver.Chrome(PATH)
# to maximize the browser window
driver.maximize_window()

# Write to csv file
def fileWriteCSV(filename, header, data):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(data)


databaseJourney = 'Microsoft Access 2013 for Beginners - Start Your Database Journey'
databaseMaster ='Microsoft Access 2013 - Advanced Master Databases'
header = ['Reg. No.', 'Email', databaseJourney, databaseMaster]
errorHeader = ['Index Number','Alison Email Address']

divider = "===================================================================================================="

currentUrl = driver.current_url
siteUrl = "https://alison.com/"
dashboardUrl = "https://alison.com/dashboard/"
loginUrl = "https://alison.com/login/"
password = "INF215$1"


def wait_for_element_to_be_clickable(element):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))

resultData = []
errorData = []

csv_file = open('files.csv')
data_set = csv_file.read()
io_string = io.StringIO(data_set)
next(io_string)

countInd = 1
for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    time.sleep(5)
    driver.get("https://alison.com/login")

    # set user email
    index_number = column[0]
    student_email = column[1]

    try:
        email = driver.find_element(By.NAME, 'email')
        password = driver.find_element(By.NAME, 'password')

        email.clear()
        email.send_keys(student_email)

        password.clear()
        password.send_keys(password)

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "submit-login")))
        elem.click()
            
        time.sleep(2)
        if driver.current_url == "https://alison.com/login":
            errorData.append(column)
            print(f'login credentials failed for {column}')
            print(divider)
            fileWriteCSV('result.csv',header,resultData)
            fileWriteCSV('error.csv',errorHeader,errorData)
            continue
        else:
            # Check if current URL is alison.com or dashboard URL
            if driver.current_url == siteUrl or driver.current_url == dashboardUrl:
                driver.get(dashboardUrl)
            else:  
                elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "alison_logo")))
                elem.click()

            time.sleep(5)
            for article in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "widget--completed"))):
                get_course_name = [my_elem.text for my_elem in WebDriverWait(article, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "widget__course-title")))]
                get_scores = [my_elem.text for my_elem in WebDriverWait(article, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "widget__score")))]

            time.sleep(2)
            # Initial a score path list and set all values to zero
            scorePath = [0,0]
            mn = [countInd, index_number,student_email]
            for course_title,score in zip(get_course_name, get_scores):
                score = int(score.rstrip(score[-1]))
                if course_title == databaseJourney:
                    scorePath[0] = score
                if course_title == databaseMaster:
                    scorePath[1] = score
            
            for x in scorePath:
                mn.append(x)
            print("success", mn)

            driver.implicitly_wait(2)
            # logout 
            driver.get("https://alison.com/logout/")
            
        countInd= countInd + 1   
        driver.implicitly_wait(2)
      
        resultData.append(mn)
        fileWriteCSV('result.csv',header,resultData)
        fileWriteCSV('error.csv',errorHeader,errorData)
    except Exception as e:
        print(e)
        driver.quit()
    
    print(divider)

# print("finally", resultData)
print(divider)
print("PROCCES IS DONE. HAMZA IS A GENIUS")
print(divider)

fileWriteCSV('result.csv',header,resultData)
fileWriteCSV('error.csv',errorHeader,errorData)
time.sleep(10)
driver.quit()

