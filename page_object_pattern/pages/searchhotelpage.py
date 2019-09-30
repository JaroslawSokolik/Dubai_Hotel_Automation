class SearchHotelPage:
    def __init__(self, driver):
        self.driver = driver

        self.search_hotel_id = "s2id_autogen8"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.click_chosen_city = "//div[contains(text(),', United Arab Emirates')]"
        self.checkin_name = "checkin"
        self.checkout_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adults_input_id = "adultInput"
        self.kids_input_id = "childInput"
        self.click_search_xpath = "//*[@id='hotels']/form/div[5]/button"

    def set_city(self, city):

        self.driver.find_element_by_id(self.search_hotel_id).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.click_chosen_city).click()

    def set_dates(self, check_in, check_out):
        self.driver.find_element_by_name(self.checkin_name).send_keys(check_in)
        self.driver.find_element_by_name(self.checkout_name).send_keys(check_out)

    def set_travellers(self, adults, kids):
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_id(self.adults_input_id).clear()
        self.driver.find_element_by_id(self.adults_input_id).send_keys(adults)
        self.driver.find_element_by_id(self.kids_input_id).clear()
        self.driver.find_element_by_id(self.kids_input_id).send_keys(kids)

    def perform_search(self):
        self.driver.find_element_by_xpath(self.click_search_xpath).click()