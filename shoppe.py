from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Lokasi driver Chrome
servis = Service('chromedriver.exe')

# Setup opsi Chrome
opsi = webdriver.ChromeOptions()
opsi.add_argument(r'---user-data-dir=C:\Users\Rahmat\AppData\Local\Google\Chrome\User Data')  # Ganti USERNAME dengan nama user PC kamu
opsi.add_argument('--profile-directory=Default')  # Ganti kalau pakai profil lain
# opsi.add_argument('--headless')  # Jangan pakai ini dulu, karena sering memicu blokir login Shopee

# Jalankan Chrome dengan Selenium
driver = webdriver.Chrome(service=servis, options=opsi)

# Buka halaman Shopee
shopee_link = 'https://shopee.co.id/search?keyword=iphone'
driver.get(shopee_link)

# Tunggu biar halaman loading
time.sleep(5)

# Simpan screenshot
driver.save_screenshot('BARU.png')

# Tutup browser
driver.quit()