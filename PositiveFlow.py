from selenium import webdriver


driver=webdriver.Chrome()
driver.get("file:///C:/Users/ruhi.shrivastava/Desktop/f1.html")
# driver.find_element_by_id("uid").send_keys("Test") -Negative Flowl
driver.find_element_by_id("xid").send_keys("Test")
driver.find_element_by_id("pid").send_keys("Test123")
driver.find_element_by_id("bid").click()