from selenium import webdriver


driver=webdriver.Chrome()
driver.get("https://www.ndtv.com/")
driver.maximize_window()
driver.implicitly_wait(30)

ele=driver.find_element_by_tag_name("ifreame")
driver.switch.to.frame(ele)


