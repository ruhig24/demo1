from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
# driver.get("https://www.cricbuzz.com/")
driver.get("https://www.tripfactory.com/")
driver.maximize_window()

#working on drop down
#creating object of select
select1 = Select(driver.find_element_by_name("excty"))

# select.select_by_value("4139")
# select.select_by_index(2)
select1.select_by_visible_text("Vadodara")

select2=Select(driver.find_element_by_name("destination"))
select2.select_by_visible_text("Singapore")


select3=Select(driver.find_element_by_name("nights"))
select3.select_by_visible_text("20 nights")

driver.find_element_by_name("hdate").clear()
driver.find_element_by_name("hdate").send_keys("12/20/2019")

print("program executed")





# driver.find_element_by_xpath("//a[text()='International']").click()
# driver.find_element_by_xpath("//a[text()='Home']").click()
# # driver.implicitly_wait(3)
# # driver.find_element_by_xpath("//*[@id='page-wrapper']/div[4]/div[1]/div[3]/div[2]/h2/a").click()
# # driver.find_element_by_xpath("//input[@name='search']").send_keys("india")
# # driver.implicitly_wait(5)
# # driver.find_element_by_xpath("//a[text()='SEARCH']").click()
# # driver.back()
# driver.find_element_by_xpath("//span[text()='ALL']").click()







