from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")

driver.find_element_by_id("s2id_autogen8").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys("Dubai")
driver.find_element_by_xpath("//div[contains(text(),', United Arab Emirates')]").click()


