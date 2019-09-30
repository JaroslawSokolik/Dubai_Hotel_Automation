from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")

driver.find_element_by_id("s2id_autogen8").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys("Dubai")
driver.find_element_by_xpath("//div[contains(text(),', United Arab Emirates')]").click()

# This is one way of choosing date
# driver.find_element_by_name("checkin").send_keys("08/10/2019")
# driver.find_element_by_name("checkout").send_keys("11/10/2019")



