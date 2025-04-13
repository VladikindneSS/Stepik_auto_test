from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

# Настроим webdriver
driver = webdriver.Chrome()

# Открываем страницу
driver.get("http://suninjuly.github.io/explicit_wait2.html")

# Дожидаемся, пока цена не станет $100
price = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

# После того как цена стала $100, нажимаем кнопку "Book"
book_button = driver.find_element(By.ID, "book")
book_button.click()

# Теперь решим математическую задачу
x_element = driver.find_element(By.ID, "input_value")
x = int(x_element.text)

# Решаем задачу
answer = str(math.log(abs(12 * math.sin(int(x)))))

# Вводим ответ в поле
answer_input = driver.find_element(By.ID, "answer")
answer_input.send_keys(answer)

# Нажимаем кнопку "Submit"
submit_button = driver.find_element(By.ID, "solve")
submit_button.click()

# Получаем число из окна
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

# Закрываем браузер
driver.quit()
