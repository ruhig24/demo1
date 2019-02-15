from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element_by_name("firstname").send_keys("Alia")
driver.find_element_by_name("lastname").send_keys("Bhatt")
driver.find_element_by_name("reg_email__").send_keys("9977422456")
driver.find_element_by_name("reg_passwd__").send_keys("abcdefg")
