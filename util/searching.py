from selenium.webdriver.common.by import By
import time
import sys


def searching(driver, text: str) -> None:
    with driver:
        driver.get("https://www.google.com/")

    # do searching
    time.sleep(3)
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys("site:blogspot.com "+text)
    search_box.submit()
    # time.sleep(3)
