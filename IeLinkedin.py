from selenium import webdriver

driver=webdriver.Ie(executable_path="C:/Users/ruhi.shrivastava/Downloads/drivers/IEDriverServer.exe")
driver.get("https://in.linkedin.com/")
driver.find_element_by_class_name("reg-firstname").send_keys("r12")
driver.find_element_by_class_name("reg-lastname").send_keys("shri12")
# driver.find_element_by_class_name("reg-email reg-field__input").send_keys("abc@gmail.com")
driver.find_element_by_id("reg-email").send_keys("abc@gmail.com")
driver.find_element_by_id("reg-password").send_keys("abcdefg")
driver.find_element_by_id("registration-submit").click()

print("program executed")
