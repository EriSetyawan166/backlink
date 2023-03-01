from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def login(email: str, pw: str, driver) -> None:

    timeout = 10
    print("logging in......")
    wait = WebDriverWait(driver, timeout)
    x = 5
    # Loads website :

    driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-1023136674%3A1675501103442719&continue=https%3A%2F%2Fwww.blogger.com%2Fhome&hl=en-US&ltmpl=blogger&rip=1&sacu=1&service=blogger&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHe7WHT1m5v5I7Ut5Ez5cj5PdHeXQ_G2nWFomBuw4BT15fvj7UooXsAagHWQAaxYRODif3NnsA")

    search = driver.find_element(By.NAME, "identifier")

    # Memasukkan credentials
    print("Filling up credentials....")
    time.sleep(x)

    search.send_keys(email)

    search.send_keys(Keys.RETURN)
    time.sleep(x)

    search = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    time.sleep(x)
    search = driver.find_element(By.NAME, "Passwd")
    search.send_keys(pw)
    search.send_keys(Keys.RETURN)
