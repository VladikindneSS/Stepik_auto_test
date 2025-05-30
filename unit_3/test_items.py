import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Для визуальной проверки языка кнопки
    add_to_cart_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_btn, "Кнопка добавления в корзину не найдена"
