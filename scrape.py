from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import time
import sys
from driver import get_chrome_option

chrome_option = get_chrome_option(True)
# Inisialisasi driver untuk mengakses browser
# driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_option)
driver = uc.Chrome(use_subprocess=True, options=chrome_option)
wait = WebDriverWait(driver, 10)

# Perintah untuk mengunjungi Google
with driver:
  driver.get("https://www.google.com/")

# Mencari elemen input pencarian di halaman
search_box = driver.find_element(By.NAME, "q")

# # Menentukan nilai x secara acak
x = 0 # Memulai dari halaman pertama
search_box.clear()
search_box.send_keys("site:blogspot.com "+sys.argv[1])

  # Menekan tombol Enter untuk melakukan pencarian
search_box.submit()

i = 1
while True:
  print("Scraping page " + str(i) + "....")
  # Mencari semua elemen link di halaman hasil pencarian
  links =  wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='yuRUbf']//a[@href]")))
  links = driver.find_elements(By.XPATH,"//div[@class='yuRUbf']//a[@href]") 

  #Membuat array untuk menyimpan link
  links_array = []
  # Memasukkan link yang didapatkan ke dalam array
  for link in links:
    link_href = link.get_attribute("href")
    if "translate" not in link_href and "webcache" not in link_href:
      links_array.append(link_href)

  # Membuat file teks untuk menyimpan link
  with open("blogspot_links.txt", "a") as file:
    for link in links_array:
      # Menulis link ke dalam file teks
      file.write(link + "\n")

  time.sleep(5)
  # Mencari tombol "Next"
  try:
    td_element = driver.find_element(By.XPATH, "//*[@id='botstuff']/div/div[2]/table/tbody/tr/td[12]")
    a_element = td_element.find_element(By.TAG_NAME, "a")
    link_next = a_element.get_attribute("href")
    driver.get(link_next)
  except Exception as e:
    print("finished")
    break

  # Increment x untuk menentukan halaman selanjutnya
  x += 10
  i = i + 1

driver.quit()
