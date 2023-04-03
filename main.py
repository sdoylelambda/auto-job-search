from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

print('START')

driver = webdriver.Chrome('../ChromeDriver/chromedriver')
# Link to search for "Software Engineer" remote jobs
search_url = 'https://www.ziprecruiter.com/jobs-search?explore_enabled=1&landed_from=suggested_jobs_blank_search&search=software+engineer&location=Remote+%28USA%29&autocomplete_request_id=957OADiwSfyiJXMWgEmBmQ'
driver.get(search_url)
time.sleep(5)

# time.sleep(5)
# driver.find_element(By.CLASS_NAME, 'modal.email_alert_modal.serp.in').click()

count = 0
pages = 1
links_to_email = []


def find_job():
    global count
    global pages
    global links_to_email

    time.sleep(5)

    # Close pop up
    try:
        driver.find_element(By.CLASS_NAME, 'modal.email_alert_modal.serp.in').click()
    except Exception as e:
        print('no pop up clicked--------')

    links = driver.find_elements(By.XPATH, '//*[@href]')
    print('links:', links)

    for link in links:
        href = link.get_attribute('href')
        if 'https://www.ziprecruiter.com/k/l' in href:
            href = link.get_attribute('href')
            links_to_email.append(href)
            count += 1
            print(href)
            time.sleep(1)

    # Close pop up
    try:
        driver.find_element(By.CLASS_NAME, 'modal.email_alert_modal.serp.in').click()
    except Exception as e:
        print('no pop up clicked--------')
        pass

    try:
        time.sleep(10)
        driver.find_element(By.CLASS_NAME, 'zrs_btn_secondary_300.load_more_btn').click()
        print('LOADING NEXT PAGE')
        pages += 1
        find_job()
    except Exception as e:
        print(f'No more pages, sending email with {count} jobs to apply on {pages} pages: {e}')
        print('links to email------>', links_to_email)  # email these to me after testing
        raise RuntimeError('END')

    time.sleep(2)  # change this after testing
    driver.close()
    driver.quit()


find_job()









jobs = [
    'https://www.ziprecruiter.com/k/l/AAJ0lzW06lrarckgpRrtr3Eo0njgBkLAozc3e7Ri7KPyvwPP47G-okyjvRfUMQNIfX_MGUv1RT2g10PO0P6NQvozFAWwHmZvRNZKuIJyYJkvz4Mf-MsBCzVLa5kZcTrj-W7PlVtTNWgVB2tAjCvRtJnAB7UW8q17gRLVOpONh3muXANZXqHWS9w7nAo2F52J-QrerA?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAK_3ah_xWAYhhx8vHpnXBi8iAU3aYYLLKC4-krDyrH5qstduKfgLiMvh2mzasmhmdJb55NUEhDVzTf448x4w2xLhMbMgSmKHmesnYy2giTLEH_-USUNQ36-yv9_Vdpx-TdACt7G8zk0ECElLQPD3isKa4ixR99a40pa8wsyJ9CFwh2AiMIFjbGbKy_MQRj86ZRY1BSQBA?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AALp-TQVPzDjn6qX-HxKpRgZwhZzZ5AU90FAeumxXZbRQ4IKfG8s-1NewQDmgdiCTPbGWGGLgrxTP168u4VoBCon14sEV5kKf-1JVW5wtfz6lXEdXB-ZWUyuP4bJ3mLtai0RPGtSuRArfq_dPQv38MKArdNnS-GMV6l8SMnfVcQh00AJ4InW9RQncC_446IImm9UtQ?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAIN1VN1mZbL3FTnfdJ7gXwDT1w8vesp12cyb_nXnUji0SwzR4OIsNxxOogqoLyLlr9Wqujpbj2nklne2oxDBbBbR5fVdHkNfTQT_xgwCeZ2Q-aZuYc5HN8u7tvmX3HB_SnwoTYfe80aJpuXIm7k9rJfKHpBaeOD7afKZz6t4yxg1oRf3qokyY8OEukqUcAx4alEcICEgg?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAJeUGhWHySioHbjx6Qjty3KYLWRVRmsqbhvB2VT7hI61BsDbgkocp7daoFNN3NPUgpi-GjZa4podOIeBGT6DMBqKKjzZtXy2BhkxP3QKb9OL5xqtMPFO9OZZtaSbxq0xGv0OlG5Fo_0mllAtcdm_3Nm0fSB4oyRI0YFYCRXUUFb64Kv_z-l1yu-DUn8Z8P1RRb0lA?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAKu0xD6L18Og_gIGfDBsXwN-4j2WyWfXAxtbZ0WsWwTeAOsRVmEHhtIB2Xqq3XCeiQpcRgzKYweb_J_zME7ovPuV9NoJ6Uv9pmaXGEp5nTpnGRNcZ3qBkyiQDHNSRlvSZmlX7roSzvRyNYVpNjGmWfRiP06lMJXee_4tZxkOjmYH77-am8Ws1VgZ6kxEgT2R4sms-o1bQ?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAKUR3yqU-v-Q24OmuTyvd19aCP7OAnIBNbyuvxTRwvp8F-N8JFa8CmvoEZs8a1LD9SzpNxfhQ0fTAht_-A8BZltMNGixIQOamPeUgt0Qf7SLr3UqNU2uplm_ZUBiwmRWGc7y4P29l9J7-LHbPBPNtpGmxnQHHGzr__3e1ZYplC9mOVnSA2XX9KfWxm7kLuuqn7xXg?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAK3hhKisYbG5QD4ThfuMLvb8yInJJn9dVZxdtP_mzSrrxFlHPLMlQWIetCAqnDGbUMMzG-eV5eYr3gy7TnPJelcl1xDs05lfH1wG5vHBchn0NRDyeh_Si04rQqncRPZ3t7nDSJdF_fCc8PcKyITELorTvHEtf5J0dHb6yIdP8j-jnUMpxmCwZkMXanG0lU7RZWilAvMQw?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAJwyTRChlzZ8_yzmSc5fGddolw8X77yws5seDwqTgdwvH9ULaMgpH5840tsld-ACgJ8Qm5MEidv_IGR-ydMR-X5YyPzkDb4Mzn3y99sxClJSzzASYUwluQlGr1mhDIWm8pM0kYI5aLeYu3k9E97jxZ6FD9saX86d5pl1wNziUWRnBsQOMq5_VUccvnGOJmMoVZcc_Y?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAIF_SLfHN9Z2fMLmT8SsAD5sNcbxcEAuJeeqaEeqbw9Tqc_jkqOuvfrRnkWOgodte2TXcxKEEl5h1dJBk1Rk2QOrZYDCRPShL1MnrD6cf19Ii4mn_6EeeYCXOvKlZ8uah2S-syv6jOJcHhpr3-9iLRZARW08CDSf6y-KfVNT3jNzpd3wn_q2wWhG8aqk4Xb2Ogm2sLcFA8?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AALTzTDyMxhI7UsckNU8Xx7O3XL27sfL0j9Aes1AZAhU6ADo5hE3Dokd2gINStcpZQaRdzQ_-l0SVrYpSiIIql052DSmp_2avDDnZz-fYjQ3HxLRPN9tYCIOvKTzcsfyJYUu2oGOn0pE5TylhVX8Xe0ly0zGrwnzAVUCYRI3bzJOIKUd_dxs7MQY1A1fGBUtlNz-Su0?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AAJWgsAWWpCJZMK2paAhbFuXdvJqiiDFYyXF-oCo1fkD0tnk-6Y2M3ClNAlH8PBazOI54OUJ5jlliuUOcYupZRbNhnr0VQfyHjmX3RjVc1XxqVaiO-AexzrduymwwVoOEHUFmMBUO39yIkAS4wHLiicY0dviiZ7Yswbc92gqsypZ1S7jUBksY5SHZ90VyMrOtJBkSM9D-8I?refu=%252Fjobs-search%253Fexplore_enabled%253D1%2526landed_from%253Dsuggested_jobs_blank_search%2526search%253Dsoftware%252Bengineer%2526location%253DRemote%252B%252528USA%252529%2526autocomplete_request_id%253D957OADiwSfyiJXMWgEmBmQ',
    'https://www.ziprecruiter.com/k/l/AALs1gur5TWIdipyJCSKwYmR5LoD9S5if9IBv8hwuMABJ8am9fW2Q_aDVHPWcKas7q4SE2FzlQRw2EiWspS4WXrwq3HhD_toAePXPSOkQN3HyDJC3bq6_36RTk8N7g39NStQvcr1F2kNniuuae9doatZtdnjpwv6D_L6UECn4Ts3fd-MDCiiOb6m1C6hTiYQJIUbrw',
    'https://www.ziprecruiter.com/k/l/AAJPg0Lwm5RaitRaTvFkx0ya8Y19ShKaZb70JzJXIX2xPuujSaM3EcvHHmUyEHRW3zlEfHDito4IRcUhP4KNVomo4u3iJgkSiZnkKxTUhIOF89XQKffQcqm4VssVbzjScvqcl4s_EGZOrNS9fdSXKD4Y1nOh990k3vMLmbs81hGdg5T13Pw1VH-9D-xkF1rHqUsBmScUwA']








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







    # quick_apply_button =
    # quick_apply_button.click()
    # Instead click the entire box
    # Grab current URL
    # Send URL to my email


# button = driver.find_element(By.CLASS_NAME, "modal-close")
# time.sleep(1)
# ActionChains(driver).move_to_element(button).click(button).perform()
# ElementClickInterceptedException: Message: element click intercepted: Element <button class=
# "zrs_btn_secondary_300 load_more_btn">...</button> is not clickable at point (297, 805). Other element would
# receive the click: <section class="modal email_alert_modal serp in" data-modal="email-alert" data-modal-state=
# "initial-mobile" tabindex="-1" role="dialog" aria-label="sign up for email job alerts"


