from selenium import webdriver
from selenium.webdriver.common.by import By


credentials = [
    {'email': 'renda89@dmxs8.com', 'password': 'renda89@dmxs8.com'},
    {'email': 'chrissilvey@dmxs8.com', 'password': 'chrissilvey@dmxs8.com'},
    {'email': 'metlina69@dmxs8.com', 'password': 'metlina69@dmxs8.com'},
    {'email': 'smudgeman@dmxs8.com', 'password': 'smudgeman@dmxs8.com'},
    {'email': 'ibarrafd@dmxs8.com', 'password': 'ibarrafd@dmxs8.com'}
]


def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


for cred in credentials:

    driver = create_driver()


    driver.get('https://ide.goorm.io/my/dashboard/')


    email = driver.find_element(By.ID, 'emailInput')
    email.clear()
    email.send_keys(cred['email'])


    password = driver.find_element(By.ID, 'passwordInput')
    password.clear()
    password.send_keys(cred['password'])


    login_button = driver.find_element(By.XPATH, "//span[contains(@class, 'Tmopq5aSmHQftHmuZSsAd')]//span[contains(text(), 'Login')]")
    login_button.click()


    driver.implicitly_wait(5)


    driver.quit()
