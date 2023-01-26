from selenium import webdriver
from selenium.webdriver.common.by import By
import random

# Inisialisasi driver untuk mengakses browser
driver = webdriver.Chrome("chromedriver.exe")

# Perintah untuk mengunjungi Google
driver.get("https://www.google.com/")


# Mencari elemen input pencarian di halaman
search_box = driver.find_element(By.NAME, "q")

# Menentukan nilai x secara acak
x = random.randint(0, 100)

# Memasukkan query pencarian ke dalam kotak pencarian
search_box.send_keys("site:blogspot.com &start=" + str(x))

# Menekan tombol Enter untuk melakukan pencarian
search_box.submit()

# Mencari semua elemen link di halaman hasil pencarian
links = driver.find_elements(By.XPATH,"//div[@class='yuRUbf']//a[@href]")

#Membuat array untuk menyimpan link
links_array = []

# Memasukkan link yang didapatkan ke dalam array
for link in links:
    links_array.append(link.get_attribute("href"))

# Membuat file teks untuk menyimpan link
with open("blogspot_links.txt", "w") as file:
    for link in links:
        # Menulis link ke dalam file teks
        file.write(link.get_attribute("href") + "\n")

# Menutup browser
driver.quit()
