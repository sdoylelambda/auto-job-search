from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def find_job():
    driver = webdriver.Chrome('../ChromeDriver/chromedriver')
    search_url = 'https://www.ziprecruiter.com/jobs-search?explore_enabled=1&landed_from=suggested_jobs_blank_search&search=software+engineer&location=Remote+%28USA%29&autocomplete_request_id=957OADiwSfyiJXMWgEmBmQ'
    driver.get(search_url)

    # link = href   https://www.ziprecruiter.com/k/l
    #
    # quick_apply_links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'ziprecruiter')
    #
    # print('quick_apply_links', quick_apply_links)
    #
    # for a in quick_apply_links:
    #     print(a)


    # elements = driver.find_elements_by_xpath("//a[contains(@href, '/mathscinet/search/mscdoc.html')]")
    # for element in elements:
    #     print(element.text)




    # quick_apply_cards = driver.find_elements(By.TAG_NAME, 'a')
    # print('quick_apply_cards', quick_apply_cards)

    links = driver.find_elements(By.XPATH, '//*[@href]')
    for link in links:
        # print(link.get_attribute('href'))
        href = link.get_attribute('href')
        if 'https://www.ziprecruiter.com/k/l' in href:
            print('YES!!!!!YES!!!!!YES!!!!!YES!!!!!YES!!!!!YES!!!!!')
            print(link.get_attribute('href'))
            href = link.get_attribute('href')



    time.sleep(2)



    #
    #
    # quick_apply_cards = driver.find_elements(By.CLASS_NAME, 'job_content')
    # print('quick_apply_cards', quick_apply_cards)
    #
    # #
    # # time.sleep(2)
    # #
    # # # traverse list
    # for quick_apply_card in quick_apply_cards:
    #     print("card::::", format(quick_apply_card))
    #     quick_apply_card_text = quick_apply_card.text
    #     # quick_apply_link = quick_apply_card.
    #     # quick_apply_link_text = quick_apply_link.text
    #     print(format(quick_apply_card_text))
    #     # print('--------------------')
    #     # print(format(quick_apply_link_text))
    #     # time.sleep(2)
    #     # links = quick_apply_card_text.getAttribute("href")
    #     # print('links', links)
    #
    #     # print(quick_apply_card.get_attribute("href"))
    #     # check string for Quick Apply
    #     if 'Quick Apply' in quick_apply_card_text:
    #         print('YES!!!!!YES!!!!!YES!!!!!YES!!!!!YES!!!!!YES!!!!!')
    #         print("href::::::::", quick_apply_card.get_attribute("href"))
    #         time.sleep(2)
            # if so email job link to me

    time.sleep(2)

    driver.close()
    driver.quit()



    # quick_apply_button =
    # quick_apply_button.click()
    # Instead click the entire box
    # Grab current URL
    # Send URL to my email



find_job()
