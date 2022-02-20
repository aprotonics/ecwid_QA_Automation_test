import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from .search_page import SearchPage
from .locators import *


class FilterPage(SearchPage):  
    def __init__(self, *args, **kwargs) -> None:
        super(FilterPage, self).__init__(*args, **kwargs)
        
        self.low_price_value = 3
        self.high_price_value = 5
        self.products_in_price_amount = 0
        self.products_in_stock_amount = 5
        self.products_with_strike_amount = 1

    def filter_by_price(self):
        self.count_products_general_amount()

        products_prices = self.driver.find_elements(*products_prices_selector)
        for price_element in products_prices:
            price = int(price_element.text.split(".")[0][1:])
            if (price >= self.low_price_value and price <= self.high_price_value):
                self.products_in_price_amount+=1
        print("In price:", self.products_in_price_amount)

        low_price = self.driver.find_element(*low_price_selector)
        low_price.send_keys(self.low_price_value)
        high_price = self.driver.find_element(*high_price_selector)
        high_price.send_keys(self.high_price_value)
        high_price.send_keys(Keys.RETURN)

        self.wait_for_filters_to_be_applied()

    def filter_by_in_stock(self):
        self.count_products_general_amount()

        print("In stock:", self.products_in_stock_amount)

        filter_by_in_stock_checkbox = self.driver.find_element(*filter_by_in_stock_checkbox_selector)
        filter_by_in_stock_checkbox.click()

        self.wait_for_filters_to_be_applied()     

    def filter_by_discount(self):
        self.count_products_general_amount()

        print("Discount:", self.products_with_strike_amount)

        filter_by_discount_checkbox = self.driver.find_element(*filter_by_discount_checkbox_selector)
        filter_by_discount_checkbox.click()

        self.wait_for_filters_to_be_applied()
    
    def check_filter_by_price(self):
        products_filtered_amount = self.count_filtered_products_amount()
        unique_products_filtered_amount = self.count_unique_products_amount()
        assert products_filtered_amount == self.products_in_price_amount
        assert unique_products_filtered_amount == self.products_in_price_amount

    def check_filter_by_in_stock(self):
        products_filtered_amount = self.count_filtered_products_amount()
        unique_products_filtered_amount = self.count_unique_products_amount()
        assert products_filtered_amount == self.products_in_stock_amount
        assert unique_products_filtered_amount == self.products_in_stock_amount
        
    def check_filter_by_discount(self):
        products_filtered_amount = self.count_filtered_products_amount()
        unique_products_filtered_amount = self.count_unique_products_amount()
        assert products_filtered_amount == self.products_with_strike_amount
        assert unique_products_filtered_amount == self.products_with_strike_amount

    def count_products_general_amount(self):
        products_general = self.driver.find_elements(*products_general_selector)
        self.products_general_amount = len(products_general)
        print("General amount of products:", self.products_general_amount)

    def count_filtered_products_amount(self):
        products_filtered = self.driver.find_elements(*products_filtered_selector)
        products_filtered_amount = len(products_filtered)
        print("Filtered products amount:", products_filtered_amount)
        return products_filtered_amount

    def count_unique_products_amount(self):
        products_names = self.driver.find_elements(*products_names_selelctor)
        products_names_set = set()
        for product_name in products_names:
            products_names_set.add(product_name.text)
        unique_products_filtered_amount = len(products_names_set)
        print("Filtered unique products amount:", unique_products_filtered_amount)
        return unique_products_filtered_amount

    def wait_for_filters_to_be_applied(self):
        time.sleep(1)
        filters_count = WebDriverWait(self.driver, 40).until(
            EC.text_to_be_present_in_element(filters_count_selector, "(1)"))
        products_container = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(products_container_selector))
        first_product = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(first_product_selector))
