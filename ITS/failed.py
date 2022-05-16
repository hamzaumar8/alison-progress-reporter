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
# driver.maximize_window()

# Write to csv file
def fileWriteCSV(filename, header, data):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(data)


errorHeader = ['Timestamp','Alison ID #:','Alison Email Address',"Student's Registration Number (UCC)"]
divider = "===================================================================================================="


password1 = "Its101$1"
errorData = []

csv_file = open('fail.csv')
data_set = csv_file.read()
io_string = io.StringIO(data_set)
next(io_string)

countInd = 1
for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    time.sleep(5)
    driver.get("https://alison.com/login")
    
    # set user email
    alision_ID = column[1]
    student_email = column[2]
    index_number = column[3]

    try:
        email = driver.find_element(By.NAME, 'email')
        password = driver.find_element(By.NAME, 'password')

        email.clear()
        email.send_keys(student_email)

        password.clear()
        password.send_keys(password1)

        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "submit-login")))
        elem.click()
            
        time.sleep(5)
        if driver.current_url == "https://alison.com/login":
            errorData.append(column)
            print(f'login credentials failed for {column}')
            print(divider)
            fileWriteCSV('error.csv',errorHeader,errorData)
        else:
            driver.get("https://alison.com/logout/")
            continue
            
    except Exception as e:
        print(e)
        driver.quit()

fileWriteCSV('error.csv',errorHeader,errorData)
print(divider)
print("PROCCES IS DONE. HAMZA IS A GENIUS")
print(divider)

time.sleep(10)

driver.quit()


# TODO:regex to check email
# TODO:check if the courses expand button has been clicked