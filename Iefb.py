from selenium import webdriver

driver=webdriver.Ie(executable_path="C:/Users/ruhi.shrivastava/Downloads/drivers/IEDriverServer.exe")

driver.get("https://www.facebook.com/")
driver.find_element_by_name("firstname").send_keys("r111rvfd")
driver.find_element_by_name("lastname").send_keys("hum12e334")
driver.find_element_by_name("reg_email__").send_keys("abc@gmail.com")
driver.find_element_by_name("reg_passwd__").send_keys("abcdefghi")
print("program executed")
