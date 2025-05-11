from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Ссылка на первую страницу (рабочую)
    #link = "http://suninjuly.github.io/registration1.html"
    # Ссылка на вторую страницу (нерабочую)
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    email.send_keys("ivan.petrov@example.com")

    # Отправка формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждём загрузки страницы
    time.sleep(1)

    # Проверка успешной регистрации
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(10)
    browser.quit()
