from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
time.sleep(4)
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input").send_keys("53920")
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]/input[1]").click()

# Switching to Alert
alert_obj=driver.switch_to.alert


# Click on Cancel button
# alert_obj.dismiss()

#Capturing text
alertMessage=alert_obj.text
print(alertMessage)

alert_obj.accept()












