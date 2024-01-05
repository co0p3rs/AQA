from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    mail = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    Phone = browser.find_element(By.CSS_SELECTOR, '.second_block .first')
    address = browser.find_element(By.CSS_SELECTOR, '.second_block .second')

    first_name.send_keys('Michael')
    last_name.send_keys('Ivanov')
    mail.send_keys('MI@mail.ru')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Ошибка'
    print('Успех')

finally:
    browser.quit()
