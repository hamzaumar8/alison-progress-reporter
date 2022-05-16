def processRun():
    if driver.current_url == siteUrl:
        driver.get(dashboardUrl)

    elif driver.current_url == dashboardUrl: 
        print("hamza baba")
    else:      
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "alison_logo"))
        )
        element.click()
        for article in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "widget__row-item"))):
            get_course_name = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "widget__course-title")))]
            get_scores = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "widget__score")))]
                
        time.sleep(2)
        for course_title,score in zip(get_course_name, get_scores):
            print(f"{student_email} - {index_number} - {course_title} - {score}")
                    

        time.sleep(2)
        # logout 
        driver.get("https://alison.com/logout/")