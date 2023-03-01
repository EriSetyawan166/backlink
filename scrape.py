import undetected_chromedriver as uc
import sys
from driver import get_chrome_option
from cookies_handler import get_cookies
from cookies_handler import use_cookies
from util import searching
from util import scraping_links
import os

# Inisialisasi driver untuk mengakses browser
chrome_option = get_chrome_option(True)
driver = uc.Chrome(use_subprocess=True, options=chrome_option)
print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░████████╗██╗░░██╗██╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║░░██║██║██╔════╝
╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝░░░██║░░░███████║██║╚█████╗░
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░░░░██║░░░██╔══██║██║░╚═══██╗
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░██║░░██║██║██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░""")

print("""\n
█▄▄ █▄█   █▀▀ █░░ █ █▀▄▀█ █▀▀ █░░ ▄▀█ █▀▄▀█
█▄█ ░█░   █▄█ █▄▄ █ █░▀░█ █▄█ █▄▄ █▀█ █░▀░█\n""")

#do scraping links
try:
    if(os.path.exists("cookies.pkl")):
      with driver:
        driver.get("https://www.google.com/")
      use_cookies(driver)
      searching(driver, sys.argv[1])
      scraping_links(driver)
    else:
      searching(driver, sys.argv[1])
      scraping_links(driver)


#handling for capthca
except Exception as e:
    driver.quit()
    chrome_option = get_chrome_option(False)    
    driver = uc.Chrome(use_subprocess=True, options=chrome_option)
    searching(driver, "testing")
    input("Press 'Enter' if you finish the captcha and google search is loaded")
    get_cookies(driver)
    driver.quit()

    #scraping the links with cookies
    try:
      chrome_option = get_chrome_option(True)
      driver = uc.Chrome(use_subprocess=True, options=chrome_option)
      with driver:
        driver.get("https://www.google.com/")
      use_cookies(driver)
      searching(driver, sys.argv[1])
      scraping_links(driver)
    except Exception as e:
      print("Somethings wrong.....")
      
driver.quit()
