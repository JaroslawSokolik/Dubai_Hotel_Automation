import pytest
from selenium import webdriver
from page_object_pattern.pages.searchhotelpage import SearchHotelPage
class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_dates("08/10/2019", "08/11/2019")
        search_hotel_page.set_travellers("2", "4")
        search_hotel_page.perform_search()




