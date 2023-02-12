from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from datetime import datetime

def send_comments(links, driver):
    # opening the file in read mode
    success = 0
    failed = 0
    timeout = 10
    wait = WebDriverWait(driver, timeout)
    my_file = open(links, "r")
    data = my_file.read()
    linkz = data.split("\n")
    total_links = len(linkz)
    print("Total links: " + str(len(linkz)))
    comment = '<a href="https://www.budiluhur.ac.id/" rel="dofollow">Thank you for the article!</a>'

    for i in range(len(linkz)):
        
        #switch cursor ke frame
        try:
            # time.sleep(3)
            print("\nLoading page " + str(i+1) + ".....")
            driver.get(linkz[i])
            start_time = time.time()
            print("finding frame....")
            # time.sleep(2)
            frame = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="comment-editor"]')))
            print("focusing to frame...")
            driver.switch_to.frame(frame)
            time.sleep(2)
            print("sending a comment...")
            search = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/div[2]/textarea')     
            # time.sleep(2)
            search.send_keys(comment)
            publish = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/div[2]/div[3]/div[1]/div/span/span')                     
            # time.sleep(2)
            publish.click()
            try:
                wait.until(EC.staleness_of(search))
                with open("report.txt", "a") as file:
                    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    file.write(f"{linkz[i]} --> berhasil\n")
                    print(f"{now}: {linkz[i]} --> berhasil")
                success = success + 1
                

            except Exception as e:
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"{now}: {linkz[i]} --> error")
                failed = failed + 1
                continue
                

        except Exception as e:
            if isinstance(e, TimeoutException):
                # Handle the timeout exception
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                elapsed_time = time.time() - start_time
                elapsed_time_in_seconds = int(elapsed_time)
                print(f"{now}: {linkz[i]} --> error timeout :{elapsed_time_in_seconds}")
                failed = failed + 1
                continue
            else:
                # Handle other generic exceptions
                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"{now}: {linkz[i]} --> error")
                failed = failed + 1
                continue
    
    return success, failed, total_links