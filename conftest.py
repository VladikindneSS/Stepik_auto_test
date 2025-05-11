import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Ваши учетные данные Stepik
LOGIN = "kundnesskung@gmail.com"
PASSWORD = "kbwtqyjvth1"

# Функция для вычисления правильного ответа
def get_answer():
    return str(math.log(int(time.time())))

# Список ссылок для параметризации теста
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    #browser.quit()

# Параметризация теста с использованием декоратора @pytest.mark.parametrize
@pytest.mark.parametrize('link', links)
def test_stepik_feedback(browser, link):
    browser.get(link)
    browser.implicitly_wait(5)

    try:
        # Авторизация
        browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login").click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "login"))).send_keys(LOGIN)
        browser.find_element(By.NAME, "password").send_keys(PASSWORD)
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

        # Ждем загрузку страницы после авторизации
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )

        # Убедимся, что страница полностью загружена и мы находимся на нужной странице
        WebDriverWait(browser, 10).until(EC.url_contains("step"))

        # Вводим ответ
        time.sleep(20)
        answer = get_answer()
        try:
            textarea = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
            textarea.clear()
            textarea.send_keys(answer)
        except Exception as e:
            print(f"Error while interacting with textarea: {e}")

        # Кнопка "Отправить"
        time.sleep(20)
        submit_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        submit_btn.click()

        # Ждем фидбек
        feedback = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )

        time.sleep(20)  # Дополнительная задержка, чтобы дождаться появления фидбека

        feedback_text = feedback.text
        print(f"Feedback text: {feedback_text}")  # Логирование текста фидбека
        assert feedback_text == "Correct!", f"Expected 'Correct!', but got '{feedback_text}'"

    except Exception as e:
        print(f"Error: {e}")
