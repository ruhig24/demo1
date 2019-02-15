from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://in.linkedin.com/")
driver.find_element_by_id("reg-firstname").send_keys("Ruhi")
driver.find_element_by_id("reg-lastname").send_keys("Shrivastava")
driver.find_element_by_id("reg-email").send_keys("rruhishrivastava536@gmail.com")
driver.find_element_by_id("reg-password").send_keys("abcdefgh")