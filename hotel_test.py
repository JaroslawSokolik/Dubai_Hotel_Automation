from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")

driver.find_element_by_id("s2id_autogen8").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys("Dubai")
driver.find_element_by_xpath("//div[contains(text(),', United Arab Emirates')]").click()
driver.find_element_by_name("checkin").send_keys("08/10/2019")
driver.find_element_by_name("checkout").send_keys("11/10/2019")
driver.find_element_by_id("travellersInput").click()
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys("4")
driver.find_element_by_id("childInput").clear()
driver.find_element_by_id("childInput").send_keys("2")
driver.find_element_by_xpath("//*[@id='hotels']/form/div[5]/button").click()

# get all h4 with class xxx and we godeeper to tag b

hotels = driver.find_elements_by_xpath("//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("hotel name is " + name)





