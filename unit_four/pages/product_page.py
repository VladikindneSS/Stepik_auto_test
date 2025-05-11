from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_product_to_basket(self):
        """Добавляет товар в корзину."""
        add_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET_BUTTON)
        )
        add_button.click()

    def get_product_name(self):
        """Возвращает название товара со страницы."""
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.PRODUCT_NAME)
        ).text

    def get_product_price(self):
        """Возвращает цену товара со страницы."""
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.PRODUCT_PRICE)
        ).text

    def should_be_success_message(self):
        """Проверяет наличие сообщения об успешном добавлении в корзину."""
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_not_be_success_message(self):
        """Проверяет отсутствие сообщения об успехе."""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        """Проверяет, что сообщение об успехе исчезает."""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"

    def should_be_correct_product_name(self):
        """Проверяет, что название товара в сообщении точно совпадает с заголовком."""
        product_name = self.get_product_name()
        success_message_name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        ).text
        print(f"Product name: '{product_name}', Success message name: '{success_message_name}'")
        assert product_name == success_message_name, \
            f"Product name '{product_name}' does not exactly match success message name '{success_message_name}'"

    def should_be_correct_basket_total(self):
        """Проверяет, что стоимость корзины совпадает с ценой товара."""
        product_price = self.get_product_price().strip()
        basket_total = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.BASKET_TOTAL)
        ).text.strip()
        print(f"Product price: '{product_price}', Basket total: '{basket_total}'")
        assert product_price == basket_total, \
            f"Basket total '{basket_total}' does not match product price '{product_price}'"