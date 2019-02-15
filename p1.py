from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get(
"https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
)
driver.find_element_by_css_selector("input#identifierId").send_keys("ruhishrivastava27@gmail.com")
# driver.find_elements_by_css_selector("")
# driver.find_element_by_xpath("//span[text()='Next']").click()
time.sleep(4)
# driver.find_element_by_xpath("//input[@name='password']").send_keys("")
# time.sleep(3)
# driver.find_element_by_xpath("//span[text()='Next']").click()
# time.sleep(4)
# driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']").click()
# driver.find_element_by_xpath("//textarea[@role='combobox']").send_keys("r")
# driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys("Selenium Testing")
# driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf']").send_keys("learning selenium and this is demo mail for practice purpose")
# driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO T-I-atl L3']").click()
# time.sleep(5)
#
# driver.find_element_by_xpath("//span[@class='gb_cb gbii']").click()
# driver.find_element_by_xpath("//a[text()='Sign out']").click()
# time.sleep(5)
# print("program executed")

