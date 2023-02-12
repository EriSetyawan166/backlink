import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

def get_chrome_option(headless: bool=False)-> Options:

    chrome_option = uc.ChromeOptions()
    prefs= {"profile.managed_default_content_settings.images": 2}
    if headless:   
        chrome_option.add_argument('--headless')
        chrome_option.add_argument('--no-sandbox')
        chrome_option.add_argument('--disable-gpu')
        chrome_option.add_argument('--window-size=1200x762')
    chrome_option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36")
    chrome_option.add_experimental_option("prefs", prefs)
    return  chrome_option