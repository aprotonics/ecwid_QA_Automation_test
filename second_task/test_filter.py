from pages.locators import *
from pages.filter_page import FilterPage


URL = "https://buy-in-10-seconds.company.site/search"


class TestFilters():
    def test_filter_by_price(self, driver):
        page = FilterPage(driver, URL)
        page.open()
        page.filter_by_price()
        page.check_filter_by_price()

    def test_filter_by_in_stock(self, driver):
        page = FilterPage(driver, URL)
        page.open()
        page.filter_by_in_stock()
        page.check_filter_by_in_stock()

    def test_filter_by_discount(self, driver):
        page = FilterPage(driver, URL)
        page.open()
        page.filter_by_discount()
        page.check_filter_by_discount()
