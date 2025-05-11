import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()  # Укажите путь к ChromeDriver, если нужно
    yield driver
    driver.quit()