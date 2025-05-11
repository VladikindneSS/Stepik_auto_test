import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.mark.parametrize("link", links)
def test_correct_feedback(browser, link):
    browser.get(link)

    # Ждём поле ответа
    textarea = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea"))
    )

    # Вводим ответ
    answer = str(math.log(int(time.time())))
    textarea.clear()
    textarea.send_keys(answer)

    # Отправляем
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

    # Ждём фидбека
    feedback = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )

    assert feedback.text == "Correct!", f"Expected 'Correct!', but got: {feedback.text}"
