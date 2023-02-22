from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

service = Service("C:/Users/Sam/Desktop/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/")

time.sleep(2)
no_login = True
while no_login:
    try:
        base_window = driver.current_window_handle
        login_button = driver.find_element(By.XPATH, '//*[@id="c-1351236777"]/div/div[1]/div/main/div[1]/div/div/div/'
                                                     'div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login_button.click()
        no_login = False
        print("logged in")
        time.sleep(7)
        options_window = driver.current_window_handle
    except NoSuchElementException:
        print("could not find log in button")
        time.sleep(2)
    else:
        no_google_option = True

        while no_google_option:
            try:
                driver.switch_to.window(options_window)
                google_login = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]')
                google_login.click()
                print("Got google option")
                no_google_option = False
            except NoSuchElementException:
                print("Waiting for google login option")
                time.sleep(2)

time.sleep(5)

driver.close()


