from selenium import webdriver

driver=webdriver.Ie(executable_path="C:/Users/ruhi.shrivastava/Downloads/drivers/IEDriverServer.exe")

driver.get("file:///C:/Users/ruhi.shrivastava/Desktop/f1.html")
driver.find_element_by_id("xid").send_keys("ruhi")

