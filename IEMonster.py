from selenium import webdriver


driver=webdriver.Ie(executable_path="C:/Users/ruhi.shrivastava/Downloads/drivers/IEDriverServer.exe")

driver.get("https://my.monsterindia.com/create_account.html?202879190349")
# driver.find_element_by_class_name("semi-bold reg-btn block uprcse").click()
driver.find_element_by_id("firstName_id").send_keys("ruh")
driver.find_element_by_id("lastName_id").send_keys("shriv")
driver.find_element_by_id("email").send_keys("ruhishrivastava27@gmail.com")
driver.find_element_by_name("passwd").send_keys("abcdefgh")

