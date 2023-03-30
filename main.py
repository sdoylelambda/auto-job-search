from selenium import webdriver
from selenium.webdriver.common.by import By


def find_job():
    driver = webdriver.Chrome('../ChromeDriver/chromedriver')
    search_url = 'https://www.ziprecruiter.com/jobs-search?explore_enabled=1&landed_from=suggested_jobs_blank_search&search=software+engineer&location=Remote+%28USA%29&autocomplete_request_id=957OADiwSfyiJXMWgEmBmQ'
    driver.get(search_url)

    # Find "Quick Apply" button but do not click it-- one option (data-tracking="quick_apply")
    # quick_apply_cards = driver.find_elements(By.NAME, "Quick Apply")

    # link = href   https://www.ziprecruiter.com/k/l

    x = driver.find_elements(By.CLASS_NAME, 'job_content')
    # links = driver.find_elements("a")
    print('x', x)

    # traverse list
    for y in x:
        # get_attribute() to get all href
        print(y)

    x = input('pause')
    driver.quit()



    # quick_apply_button =
    # quick_apply_button.click()
    # Instead click the entire box
    # Grab current URL
    # Send URL to my email



find_job()
