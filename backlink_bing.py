import undetected_chromedriver as uc
from dotenv import load_dotenv
import os
from driver import get_chrome_option
from cookies_handler import get_cookies_login
from cookies_handler import use_cookies_login
from util import login
from util import send_comments
import time

start_time = time.time()
print("""
██████╗░░█████╗░░█████╗░██╗░░██╗██╗░░░░░██╗███╗░░██╗██╗░░██╗  ██████╗░░█████╗░████████╗██████╗░░░░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║░░░░░██║████╗░██║██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝╚════██╗░░░██╔══██╗
██████╦╝███████║██║░░╚═╝█████═╝░██║░░░░░██║██╔██╗██║█████═╝░  ██████╦╝██║░░██║░░░██║░░░░░███╔═╝░░░██║░░██║
██╔══██╗██╔══██║██║░░██╗██╔═██╗░██║░░░░░██║██║╚████║██╔═██╗░  ██╔══██╗██║░░██║░░░██║░░░██╔══╝░░░░░██║░░██║
██████╦╝██║░░██║╚█████╔╝██║░╚██╗███████╗██║██║░╚███║██║░╚██╗  ██████╦╝╚█████╔╝░░░██║░░░███████╗██╗╚█████╔╝
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░╚════╝░""")

print("""\n
█▄▄ █▄█   █▀▀ █░░ █ █▀▄▀█ █▀▀ █░░ ▄▀█ █▀▄▀█
█▄█ ░█░   █▄█ █▄▄ █ █░▀░█ █▄█ █▄▄ █▀█ █░▀░█\n""")

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
print("opening chrome....")
chrome_option = get_chrome_option(True)
driver = uc.Chrome(use_subprocess=True,options=chrome_option)

try:    
    if(os.path.exists("cookies_login.pkl")):
        print("Logging in....")
        use_cookies_login(driver)
        success, failed, total_links = send_comments("blogspot_links.txt",driver)
    else:
        raise Exception("Cookies not found")
        # login(EMAIL, PASSWORD, driver)
        # success, failed, total_links = send_comments("blogspot_links.txt",driver)

except Exception as e:
    driver.quit()
    chrome_option = get_chrome_option(False)
    driver = uc.Chrome(use_subprocess=True,options=chrome_option)
    driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-1023136674%3A1675501103442719&continue=https%3A%2F%2Fwww.blogger.com%2Fhome&hl=en-US&ltmpl=blogger&rip=1&sacu=1&service=blogger&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHe7WHT1m5v5I7Ut5Ez5cj5PdHeXQ_G2nWFomBuw4BT15fvj7UooXsAagHWQAaxYRODif3NnsA")
    print("Please login manually ")
    input("Press 'Enter' if you finish login in manually UwU")
    get_cookies_login(driver)
    driver.quit()

    try:
        chrome_option = get_chrome_option(True)
        driver = uc.Chrome(use_subprocess=True,options=chrome_option)
        use_cookies_login(driver)
        success, failed, total_links = send_comments("blogspot_links.txt",driver)
    
    except Exception as e:
        print("Something's wrong when logging in....")
        print("Check your internet, your account...")
        print("Probably captcha is causing this error")
        print("if so, try again later....")
        print("you can try to use nonheadless chrome by setting the boolean to false to check if there's appear authentication:")
        print("chrome_option = get_chrome_option(False)")
        print("after finishing verification try using headless again by changing it to True")

driver.quit()

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Convert the elapsed time to a string in the format "HH:MM:SS"
elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

print("\nFinished......")
print("Total links: " + str(total_links))
print("Success: " + str(success))
print("Failed: " + str(failed))
print("Elapsed time:", elapsed_time_str)