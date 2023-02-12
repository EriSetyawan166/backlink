from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def scraping_links(driver) -> None:
    wait = WebDriverWait(driver, 10)
    x = 0 
    i = 1

    while True:
        links_array = []
        #scraping the link
        print("Scraping page " + str(i) + "....")
       
        links =  wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='yuRUbf']//a[@href]")))
    
        # get_cookies(driver)
        links = driver.find_elements(By.XPATH,"//div[@class='yuRUbf']//a[@href]") 
        
        #preprocessing the links
        for link in links:
            link_href = link.get_attribute("href")
            if "translate" not in link_href and "webcache" not in link_href and "google.com/search?" not in link_href:
                links_array.append(link_href)

        #saving the links
        with open("blogspot_links.txt", "a") as file:
            for link in links_array:
                # Menulis link ke dalam file teks
                file.write(link + "\n")

        # time.sleep(5)

        #go the next page
        try:
            td_element = driver.find_element(By.XPATH, "//*[@id='botstuff']/div/div[2]/table/tbody/tr/td[12]")
            a_element = td_element.find_element(By.TAG_NAME, "a")
            link_next = a_element.get_attribute("href")
            driver.get(link_next)
        except Exception as e:
            try:
                td_element = driver.find_element(By.XPATH, "//*[@id='botstuff']/div/div[2]/table/tbody/tr/td[4]")
                a_element = td_element.find_element(By.TAG_NAME, "a")
                link_next = a_element.get_attribute("href")
                driver.get(link_next)
            except Exception as e:
                print("finished")
                if i == 1:
                    print("Only getting 1 page links, try again if you think that it's not true")
                break
       
        x += 10
        i = i + 1

    unique_links = {}

    with open("blogspot_links.txt", "r") as file:
        links = file.readlines()

    for link in links:
        link = link.strip() # Menghapus spasi pada awal dan akhir link
        domain = link.split("//")[-1].split("/")[0] # Mendapatkan domain dari link
        if domain not in unique_links:
            unique_links[domain] = link

        # Menuliskan set yang berisi link unik ke file baru
    with open("blogspot_links.txt", "w") as file:
        file.write("")
        for link in unique_links.values():
            file.write(link + "\n")