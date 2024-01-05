from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

link = "http://suninjuly.github.io/registration2.html"
driver = webdriver.Chrome()
try:
    driver.get(link)
    css = 'input.form-control[type="text"][placeholder^="Input your"]'
    elements = driver.find_elements(By.CSS_SELECTOR, css)
    for element in elements:
        s = string.ascii_lowercase + string.ascii_uppercase + string.digits
        element.send_keys(''.join([random.choice(s) for _ in range(random.randint(8, 16))]))
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    for _ in range(60):
        s = "Congratulations! You have successfully registered!"
        if driver.find_element(By.CSS_SELECTOR, 'div.container h1').text.strip() == s:
            break
        time.sleep(0.1)
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    driver.quit()
