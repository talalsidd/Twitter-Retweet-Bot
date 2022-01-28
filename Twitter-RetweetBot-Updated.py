from getpass import getpass
import time
import re
from random import *
import random,string
from turtle import title
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
#options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
#options.add_argument('--disable-gpu')
#options.add_argument('--headless')
#options.add_argument('disable-notifications')
email = input("Please enter you Email: ")
username_phonenumber = input("Please enter your Twitter Username or Phonenumber: ")
password = getpass("Please enter your Password: ")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) 

#driver.maximize_window()
driver.implicitly_wait(100)
driver.get("https://twitter.com/i/flow/login")
#driver.maximize_window()

def tweetpage():
    try:
        #myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
        #print("Page is ready!")
        #element = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]'))
        #)
        time.sleep(6)
        driver.find_element(By.CSS_SELECTOR,'input[autocomplete="username"]').click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,'input[autocomplete="username"]').send_keys(email)
        time.sleep(2)
        driver.implicitly_wait(100)
        driver.find_element(By.CSS_SELECTOR,'input[autocomplete="username"]').send_keys(u'\ue007')
        driver.implicitly_wait(100)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'div>input').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'div>input').send_keys(username_phonenumber)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'div>input').send_keys(u'\ue007')
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'[type="password"]').send_keys(password)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'[type="password"]').send_keys(u'\ue007')
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 500)")
        driver.implicitly_wait(10)
        #t1 = driver.find_elements(By.XPATH,'//*[@data-testid="reply"]')
        #tweets = driver.find_elements(By.CSS_SELECTOR,'[aria-label="Timeline: Your Home Timeline"]>div>div article a[href*="/status/"][dir="auto"]')
        time.sleep(5)
        while True:
            stringarray=[]
            for i in range(1,4):
                time.sleep(2)
                hash = "#"
                try:
                    tweetmaterial = driver.find_element(By.CSS_SELECTOR,'div[class="css-1dbjc4n"][aria-label="Timeline: Your Home Timeline"]>div>div:nth-of-type('+str(i)+') article div[lang]').text
                    print(tweetmaterial)
                    if tweetmaterial not in stringarray:
                        stringarray.append(tweetmaterial)
                        if hash in tweetmaterial:
                            driver.implicitly_wait(100)
                            driver.execute_script("window.scrollTo(0, 100)")
                            time.sleep(3)
                            driver.execute_script("""window.document.querySelector('div[class="css-1dbjc4n"][aria-label="Timeline: Your Home Timeline"]>div>div:nth-of-type("""+str(i)+""") article  div:nth-child(1) > div[data-testid="reply"] div[dir="ltr"]>div').click()""")
                            time.sleep(3)
                            driver.implicitly_wait(100)
                            driver.find_element(By.CSS_SELECTOR,'[aria-labelledby="modal-header"]  div[class="DraftEditor-editorContainer"] [aria-label="Tweet text"]').send_keys("your wish is granted")
                            time.sleep(5)
                            driver.execute_script("""document.querySelector('[aria-labelledby="modal-header"]  div[data-testid="toolBar"] [aria-label="Add a GIF"]').click()""")
                            #clickable = driver.find_element(By.XPATH,'//*[@aria-label="Add a GIF"]')
                            #clickable.click
                            time.sleep(3)
                            driver.execute_script("""document.querySelector("[class='css-1dbjc4n']>div[class*='r-1mnahxq']>div:nth-of-type(2)").click()""")
                            #driver.find_element(By.CSS_SELECTOR,'[class="css-1dbjc4n"]>div[class*="r-1mnahxq"]>div:nth-of-type(2)').click
                            time.sleep(2)
                            driver.execute_script("""document.querySelector('div[data-testid="gifSearchGifImage"]:nth-of-type(1)').click()""")
                            #driver.find_element(By.CSS_SELECTOR,'div[data-testid="gifSearchGifImage"]:nth-of-type(1)').click
                            time.sleep(2)
                            driver.execute_script("""document.querySelector('[aria-labelledby="modal-header"]  div[data-testid="toolBar"] [data-testid="tweetButton"]').click()""")
                            #clickbutton = driver.find_element(By.CSS_SELECTOR,'div[data-testid="tweetButtonInline"]').click
                            time.sleep(8)
                            driver.execute_script("""document.querySelector('[aria-labelledby="modal-header"] [data-testid="app-bar-close"]').click()""")
                            i=i+1
                            time.sleep(2)
                            continue
                        else:
                            print('No hashtag found')
                            continue
                    else:
                        continue
                except:
                    print("No article")
                    continue
            time.sleep(40)
            driver.execute_script("""window.location.reload()""")
            time.sleep(3)

    except TimeoutException:
        print("Loading took too much time!")
if driver.find_element(By.CSS_SELECTOR,'[data-testid="confirmationSheetDialog"]'):
    driver.execute_script("""window.document.querySelector('[data-testid="confirmationSheetDialog"] [data-testid="confirmationSheetConfirm"]').click()""")
    time.sleep(3)
    driver.execute_script("""window.document.querySelector('[data-testid="loginButton"]').click()""")
    time.sleep(3)
    tweetpage()
else:
    tweetpage()   

                        
         
        

   



