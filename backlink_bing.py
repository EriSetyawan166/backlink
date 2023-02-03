from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random, time
import undetected_chromedriver as uc
from datetime import datetime
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import hashlib
import random
BASE_PATH = os.getcwd()
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def get_chrome_option(headless: bool=False)-> Options:

    chrome_option = uc.ChromeOptions()
    if headless:
        chrome_option.add_argument('--headless')
        chrome_option.add_argument('--no-sandbox')
        chrome_option.add_argument('--disable-gpu')
        chrome_option.add_argument('--window-size=1200x762')
    chrome_option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36")
    
    return  chrome_option


timeout = 10
# datetime object containing current date and time
now = datetime.now()
#Membuat array untuk menyimpan link
links_array = []
#Import chromedriver
chrome_option = get_chrome_option(True)
driver = uc.Chrome(use_subprocess=True, options=chrome_option)

driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_option) 

def dump_html(html_text: str):
    path = BASE_PATH

    string_file = str(123)
    print(string_file)
    file_name = hashlib.sha256(string_file.encode("utf-8")).hexdigest()

    file_extension = ".html"

    file = path + file_name + file_extension

    with open(file, "wb") as f:
        f.write(html_text.encode("utf-8"))

    return file

def login_blogger(email,pw,txt):
    print("logging in......")
    wait = WebDriverWait(driver, timeout)
    x = 5
    #Loads website :
    driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S1494194976%3A1675447820795540&continue=https%3A%2F%2Fwww.blogger.com%2Fhome%23create&hl=en-US&ltmpl=blogger&rip=1&sacu=1&service=blogger&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHe3QQ0ZorrvHXHsoIJN5jlzc-IK7ngCixzmmB9W6o4Zek-CZyBL8neYz_yQCytXIwtb8qxJtA")
    time.sleep(x)

    search = driver.find_element(By.NAME,"identifier")
    # Memasukkan credentials
    print("Filling up credentials....")
    time.sleep(x)
    
    search.send_keys(email)
    
    search.send_keys(Keys.RETURN)
    time.sleep(x)
    # file = dump_html(driver.page_source)
    
    # html_content = driver.page_source

    # # Mencetak HTML source ke console
    # print(html_content)
    search = wait.until(EC.presence_of_element_located((By.NAME,"Passwd")))
    time.sleep(x)
    search = driver.find_element(By.NAME,"Passwd")
    search.send_keys(pw)
    search.send_keys(Keys.RETURN)
        
    time.sleep(20)
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
            print("Loading the page....")
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

login_blogger(EMAIL, PASSWORD, "links.txt")