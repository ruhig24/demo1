from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.find_element_by_xpath("//input[@class='orangeBtn bifurLightBox']").click()
driver.find_elements_by_xpath("//button[@class='action-btn exp']").click()

