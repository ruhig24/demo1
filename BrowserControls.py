from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_class_name("chNavText darkGreyText").click()
time.sleep(5)
driver.find_element_by_id("header_tab_holidays").click()

time.sleep(5)
driver.back()
time.sleep(3)
driver.forward()


