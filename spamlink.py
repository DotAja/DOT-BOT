import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

github_proxy_url = 'https://raw.githubusercontent.com/DotAja/DOT-BOT/main/memek.txt'

response = requests.get(github_proxy_url)

proxy_list = response.text.splitlines()

extension_path = 'Socks5 Configurator 2023.6.12.0.crx'

chrome_options = Options()
chrome_options.add_extension(extension_path)

for i in range(5):
    for proxy in proxy_list:

        driver = webdriver.Chrome(options=chrome_options)

        time.sleep(5)

        driver.get("chrome-extension://hnpgnjkeaobghpjjhaiemlahikgmnghb/options.html")

        time.sleep(2)

        proxy_input = driver.find_element(By.XPATH, "//input[@aria-label='Example: 127.0.0.1:1080 or [::1]:1080']")
        proxy_input.clear()
        proxy_input.send_keys(proxy)

        time.sleep(1)

        save_button = driver.find_element(By.XPATH, "//wl-button[@id='save']")
        save_button.click()

        time.sleep(2)

        for _ in range(3):
            driver.execute_script("window.open('https://ignateignatetame.com/pbv2016jd1?key=a7a3b72cce96c3d676e783729b9f4501', '_blank')")
            time.sleep(1)

        time.sleep(60)

        driver.quit()
