from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.select import Select
import time
#From one browser to another browser
# driver=webdriver.Chrome()
# 1.Browser Control
# driver.get("https://www.makemytrip.com/")
# driver.maximize_window()
# driver.implicitly_wait(30)
# driver.find_element_by_xpath("//span[text()='Flights']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//span[text()='Holidays']").click()
#
# time.sleep(5)
# driver.back()
# time.sleep(3)
# driver.forward()

#Multiple browser
# browser='chrome'
#
# if browser=='chrome':
#     driver=webdriver.Chrome()
# elif browser=='ie':
#     driver=webdriver.Ie(executable_path="C:/Users/ruhi.shrivastava/Downloads/drivers/IEDriverServer.exe)")
# driver.get("https://www.goibibo.com/")
# driver.implicitly_wait(20)
# driver.maximize_window()


#Select goibibo
driver=webdriver.Chrome()
driver.get("https://www.goibibo.com/")
driver.implicitly_wait(30)
driver.maximize_window()

driver.find_element(By.ID,"gosuggest_inputSrc").send_keys("Gwalior (GWL)")


driver.find_element(By.ID,"gosuggest_inputDest").send_keys("Bangalore (BLR)")


wait = WebDriverWait(driver, 30 );


driver.find_element(By.XPATH,"//*[@id='searchWidgetCommon']/div[1]/div[1]/div[1]/div/div[6]/input ").send_keys("7/24/2019")


