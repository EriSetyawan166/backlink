import pickle
import time

def get_cookies(driver) -> None:
    cookies = driver.get_cookies()
    pickle.dump(cookies, open("cookies.pkl", "wb"))

def use_cookies(driver) -> None:
    cookies = pickle.load(open("cookies.pkl", "rb"))

    for cookie in cookies:
      cookie['domain'] = ".google.com"

      try: 
        driver.add_cookie(cookie)
      except Exception as e:
        print(e)

    driver.get("https://www.google.com/")

def get_cookies_login(driver) -> None:
    time.sleep(5)
    cookies = driver.get_cookies()
    pickle.dump(cookies, open("cookies_login.pkl", "wb"))

def use_cookies_login(driver) -> None:
    driver.get("https://www.blogger.com/")
    time.sleep(5)
    cookies = pickle.load(open("cookies_login.pkl", "rb"))

    for cookie in cookies:
        # cookie['domain'] = ".blogger.com"

        try: 
            driver.add_cookie(cookie)
        except Exception as e:
            print(e)

    driver.get("https://www.blogger.com/blog/posts/3799933515691905805")