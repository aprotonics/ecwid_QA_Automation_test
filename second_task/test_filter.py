import time
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# For Chromium
from webdriver_manager.utils import ChromeType

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


URL = "https://buy-in-10-seconds.company.site/search"


# @unittest.skip
class TestFilterChrome(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--remote-debugging-port=9222")

        # For Chrome
        # service=Service(ChromeDriverManager().install())

        # For Chromium
        service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        driver = webdriver.Chrome(service=service, options=options)

        # driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)
        self.driver = driver

    def test_filter_by_price(self):
        driver = self.driver

        low_price_value = 3
        high_price_value = 5

        products_general = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_general_amount = len(products_general)
        print("General by price", products_general_amount)

        products_prices = driver.find_elements(By.XPATH, '//*[contains(@class, "ec-price-item")]')
        products_in_price_number = 0
        for price_element in products_prices:
            price = int(price_element.text.split(".")[0][1:])
            if (price >= low_price_value and price <= high_price_value):
                products_in_price_number+=1
        print("In price ", products_in_price_number)

        low_price = driver.find_element(By.XPATH, '(//div[contains(@class, "ec-filter__price-wrap")]//input)[1]')
        low_price.send_keys(low_price_value)
        high_price = driver.find_element(By.XPATH, '(//div[contains(@class, "ec-filter__price-wrap")]//input)[2]')
        high_price.send_keys(high_price_value)
        high_price.send_keys(Keys.RETURN)

        time.sleep(1)

        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(@class, "ec-filters__applied-count")]'), "(1)"))
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "grid__products")]')))
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "grid__product")]/div[1]')))

        products_filtered = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_filtered_amount = len(products_filtered)
        print("In price ", products_filtered_amount)

        self.assertEqual(products_in_price_number, products_filtered_amount)
    
    def test_filter_by_in_stock(self):
        driver = self.driver
        products_general = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_general_amount = len(products_general)
        print("General in stock", products_general_amount)
        products_not_in_stock = driver.find_elements(By.XPATH, '//div[contains(@class, "label__text") and contains(text(), "Распродано")]')
        products_not_in_stock_amount = len(products_not_in_stock)
        products_in_stock_amount = products_general_amount - products_not_in_stock_amount
        print("In stock ", products_in_stock_amount)

        filter_checkbox = driver.find_element(By.XPATH, '//*[@id="checkbox-in_stock"]')
        filter_checkbox.click()

        time.sleep(1)

        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(@class, "ec-filters__applied-count")]'), "(1)"))
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "grid__products")]')))
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "grid__product")]/div[1]')))

        products_filtered = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_filtered_amount = len(products_filtered)
        print("In stock ", products_filtered_amount)

        self.assertEqual(products_in_stock_amount, products_filtered_amount)

    def test_filter_by_discount(self):
        driver = self.driver
        products_general = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_general_amount = len(products_general)
        print("General discount", products_general_amount)
        products_with_strike = driver.find_elements(By.XPATH, '//strike')
        products_with_strike_amount = len(products_with_strike)
        print("Discount ", products_with_strike_amount)

        filter_checkbox = driver.find_element(By.XPATH, '//*[@id="checkbox-on_sale"]')
        filter_checkbox.click()

        time.sleep(1)

        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(@class, "ec-filters__applied-count")]'), "(1)"))
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "grid__products")]')))
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "grid__product")]/div[1]')))
        products_filtered = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_filtered_amount = len(products_filtered)
        print("Discount ", products_filtered_amount)

        self.assertEqual(products_with_strike_amount, products_filtered_amount)

    def tearDown(self):
        self.driver.quit()

@unittest.skip
class TestFilterFirefox(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        options.add_argument('--ignore-certificate-errors')

        service=Service(GeckoDriverManager().install())

        driver = webdriver.Firefox(service=service, options=options)

        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)
        self.driver = driver

    def test_filter_by_price(self):
        driver = self.driver

        low_price_value = 3
        high_price_value = 5

        products_general = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_general_amount = len(products_general)
        print("General by price", products_general_amount)

        products_prices = driver.find_elements(By.XPATH, '//*[contains(@class, "ec-price-item")]')
        products_in_price_number = 0
        for price_element in products_prices:
            price = int(price_element.text.split(".")[0][1:])
            if (price >= low_price_value and price <= high_price_value):
                products_in_price_number+=1
        print("In price ", products_in_price_number)

        low_price = driver.find_element(By.XPATH, '(//div[contains(@class, "ec-filter__price-wrap")]//input)[1]')
        low_price.send_keys(low_price_value)
        high_price = driver.find_element(By.XPATH, '(//div[contains(@class, "ec-filter__price-wrap")]//input)[2]')
        high_price.send_keys(high_price_value)
        high_price.send_keys(Keys.RETURN)

        time.sleep(1)

        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(@class, "ec-filters__applied-count")]'), "(1)"))
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "grid__products")]')))
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "grid__product")]/div[1]')))

        products_filtered = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_filtered_amount = len(products_filtered)
        print("In price ", products_filtered_amount)

        self.assertEqual(products_in_price_number, products_filtered_amount)
    
    def test_filter_by_in_stock(self):
        driver = self.driver
        products_general = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_general_amount = len(products_general)
        print("General in stock", products_general_amount)
        products_not_in_stock = driver.find_elements(By.XPATH, '//div[contains(@class, "label__text") and contains(text(), "Распродано")]')
        products_not_in_stock_amount = len(products_not_in_stock)
        products_in_stock_amount = products_general_amount - products_not_in_stock_amount
        print("In stock ", products_in_stock_amount)

        filter_checkbox = driver.find_element(By.XPATH, '//*[@id="checkbox-in_stock"]')
        filter_checkbox.click()

        time.sleep(1)

        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(@class, "ec-filters__applied-count")]'), "(1)"))
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "grid__products")]')))
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "grid__product")]/div[1]')))

        products_filtered = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_filtered_amount = len(products_filtered)
        print("In stock ", products_filtered_amount)

        self.assertEqual(products_in_stock_amount, products_filtered_amount)

    def test_filter_by_discount(self):
        driver = self.driver
        products_general = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_general_amount = len(products_general)
        print("General discount", products_general_amount)
        products_with_strike = driver.find_elements(By.XPATH, '//strike')
        products_with_strike_amount = len(products_with_strike)
        print("Discount ", products_with_strike_amount)

        filter_checkbox = driver.find_element(By.XPATH, '//*[@id="checkbox-on_sale"]')
        filter_checkbox.click()

        time.sleep(1)

        WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element((By.XPATH, '//*[contains(@class, "ec-filters__applied-count")]'), "(1)"))
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "grid__products")]')))
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "grid__product")]/div[1]')))
        products_filtered = driver.find_elements(By.XPATH, '//div[contains(@class, "grid__product")]/div')
        products_filtered_amount = len(products_filtered)
        print("Discount ", products_filtered_amount)

        self.assertEqual(products_with_strike_amount, products_filtered_amount)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
