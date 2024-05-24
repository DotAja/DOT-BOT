from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# Ambil daftar proxy dari URL
proxy_url = "https://raw.githubusercontent.com/DotAja/DOT-BOT/main/memek.txt"
proxies = requests.get(proxy_url).text.strip().split("\n")

# Fungsi untuk membuat driver Selenium dengan proxy
def create_driver(proxy):
    options = webdriver.ChromeOptions()

    if proxy.startswith('socks'):
        options.add_argument('--proxy-server=socks5://%s' % proxy)
    else:
        options.add_argument('--proxy-server=http://%s' % proxy)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://ignateignatetame.com/pbv2016jd1?key=a7a3b72cce96c3d676e783729b9f4501')
    return driver

# Loop melalui daftar email
for i, email in enumerate(emails):
    # Hitung indeks proxy
    proxy_index = i % len(proxies)
    proxy = proxies[proxy_index]

    # Buat driver dengan proxy
    driver = create_driver(proxy)

    # Tunggu 60 detik (atau lebih lama sesuai kebutuhan)
    time.sleep(60)

    # Tutup driver
    driver.quit()
