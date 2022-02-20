from selenium.webdriver.common.by import By


products_general_selector = (By.XPATH, '//div[contains(@class, "grid__product")]/div')
products_prices_selector = (By.XPATH, '//*[contains(@class, "ec-price-item")]')
low_price_selector = (By.XPATH, '(//div[contains(@class, "ec-filter__price-wrap")]//input)[1]')
high_price_selector = (By.XPATH, '(//div[contains(@class, "ec-filter__price-wrap")]//input)[2]')
filters_count_selector = (By.XPATH, '//*[contains(@class, "ec-filters__applied-count")]')
products_container_selector = (By.XPATH, '//div[contains(@class, "grid__products")]')
first_product_selector = (By.XPATH, '//div[contains(@class, "grid__product")]/div[1]')
products_filtered_selector = (By.XPATH, '//div[contains(@class, "grid__product")]/div')
products_names_selelctor = (By.XPATH, '//div[contains(@class, "grid-product__title-inner")]')
filter_by_in_stock_checkbox_selector = (By.XPATH, '//*[@id="checkbox-in_stock"]')
filter_by_discount_checkbox_selector = (By.XPATH, '//*[@id="checkbox-on_sale"]')
