from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random, time
import undetected_chromedriver as uc
from datetime import datetime
import time
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
import os
from debugging import dump_html
from driver import get_chrome_option
import random

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
timeout = 10
# datetime object containing current date and time
now = datetime.now()
#Membuat array untuk menyimpan link
links_array = []
#Import chromedriver
chrome_option = get_chrome_option(True)
driver = uc.Chrome(use_subprocess=True, options=chrome_option)

# driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_option) 

def login_blogger(email,pw,txt):
    try:
        print("logging in......")
        wait = WebDriverWait(driver, timeout)
        x = 5
        #Loads website :
        with driver:
            driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S1494194976%3A1675447820795540&continue=https%3A%2F%2Fwww.blogger.com%2Fhome%23create&hl=en-US&ltmpl=blogger&rip=1&sacu=1&service=blogger&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHe3QQ0ZorrvHXHsoIJN5jlzc-IK7ngCixzmmB9W6o4Zek-CZyBL8neYz_yQCytXIwtb8qxJtA")
        time.sleep(x)

        search = driver.find_element(By.NAME,"identifier")
        # Memasukkan credentials
        print("Filling up credentials....")
        time.sleep(x)
        
        search.send_keys(email)
        
        search.send_keys(Keys.RETURN)
        time.sleep(x)
        file = dump_html(driver.page_source)
        
        # html_content = driver.page_source

        # # Mencetak HTML source ke console
        # print(html_content)
        search = wait.until(EC.presence_of_element_located((By.NAME,"Passwd")))
        time.sleep(x)
        search = driver.find_element(By.NAME,"Passwd")
        search.send_keys(pw)
        search.send_keys(Keys.RETURN)
    
    except Exception as e:
        print("Something's wrong when logging in....")
        print("Check you internet, your account...")
        print("Probably captcha is causing this error")
        print("you can try to use nonheadless chrome by setting the boolean to false to check if there's appear authentication:")
        print("chrome_option = get_chrome_option(False)")
        return

        
    time.sleep(30)
    # opening the file in read mode
    my_file = open(txt, "r")
    data = my_file.read()
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    linkz = data.split("\n")
    comment = '<a href="https://www.budiluhur.ac.id/" rel="dofollow">Thank you for the article!</a>'

    

    for i in range(len(linkz)):
        r = random.randint(0, 2)
        
        #switch cursor ke frame
        try:
            time.sleep(3)
            print("\nLoading the page....")
            driver.get(linkz[i])
            start_time = time.time()
            print("finding frame....")
            time.sleep(2)
            frame = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="comment-editor"]')))
            print("focusing to frame...")
            driver.switch_to.frame(frame)
            time.sleep(2)
            print("sending a comment...")
            search = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/div[2]/textarea')     
            search.send_keys(comment)
            time.sleep(2) 
            publish = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/div[2]/div[3]/div[1]/div/span/span')                     
            publish.click()
            try:
                wait.until(EC.staleness_of(search))
                with open("report.txt", "a") as file:
                    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    file.write(f"{linkz[i]} --> berhasil\n")
                    print(f"{now}: {linkz[i]} --> berhasil")
                

            except Exception as e:
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"{now}: {linkz[i]} --> error")
                continue
                

        except Exception as e:
            if isinstance(e, TimeoutException):
                # Handle the timeout exception
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                elapsed_time = time.time() - start_time
                elapsed_time_in_seconds = int(elapsed_time)
                print(f"{now}: {linkz[i]} --> error timeout :{elapsed_time_in_seconds}")
                continue
            else:
                # Handle other generic exceptions
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"{now}: {linkz[i]} --> error")
                continue

login_blogger(EMAIL, PASSWORD, "blogspot_links.txt")