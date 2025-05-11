import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language", 
        action="store", 
        default="en", 
        help="Choose language: e.g. en, es, fr"
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    print(f"\nStarting Chrome for language: {user_language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuitting browser...")
    try:
        browser.quit()
    except Exception as e:
        print(f"Error closing browser: {e}")
