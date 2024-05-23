from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

proxy_url = "https://raw.githubusercontent.com/DotAja/DOT-BOT/main/memek.txt"
credentials_url = "https://raw.githubusercontent.com/DotAja/DOT-BOT/main/kontol.txt"

proxies = requests.get(proxy_url).text.strip().split("\n")
emails = requests.get(credentials_url).text.strip().split("\n")

def create_driver(proxy):
    options = webdriver.ChromeOptions()

    if proxy.startswith('socks'):
        options.add_argument('--proxy-server=socks5://%s' % proxy)
    else:
        options.add_argument('--proxy-server=http://%s' % proxy)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://ide.goorm.io/my/dashboard/')
    return driver

for i, email in enumerate(emails):
    proxy_index = i % len(proxies)
    proxy = proxies[proxy_index]

    driver = create_driver(proxy)

    email_input = driver.find_element(By.ID, 'emailInput')
    password_input = driver.find_element(By.ID, 'passwordInput')

    email_input.clear()
    password_input.clear()

    email_input.send_keys(email)
    password_input.send_keys(email)

    login_button = driver.find_element(By.XPATH, "//span[contains(@class, 'Tmopq5aSmHQftHmuZSsAd')]//span[contains(text(), 'Login')]")
    login_button.click()

    time.sleep(30)

    close_button = driver.find_element(By.XPATH, "//div[@class='modal-content']//button[@aria-label='Close']")
    close_button.click()

    time.sleep(2)
    
    create_resource_button = driver.find_element(By.ID, "hibernate_cardRun_dInv3CY5igiBpyMoV2A")
    create_resource_button.click()

    driver.quit()
