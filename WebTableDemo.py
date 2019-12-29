from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/ruhi.shrivastava/Desktop/html%20page/webtable.html")
driver.maximize_window()
driver.implicitly_wait(30)

# cell_val=driver.find_element_by_xpath("//*[@id='emp']/tbody/tr[1]/td[1]")
# print(cell_val.text)

# row_val=driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr[1]/td")
# print(row_val)
# print(type(row_val))
# for val in row_val:
#     print(val.text)


# #third row data
# row_val=driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr[3]/td")
# print(row_val)
# print(type(row_val))
# for val in row_val:
#     print(val.text)


#2nd row data
# row_val=driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr[2]/td")
# print(row_val)
# print(type(row_val))
# for val in row_val:
#     print(val.text)


#Entire table data
# entire_val=driver.find_elements_by_xpath("//*[@id='emp']/tbody")
# print(entire_val)
# for val in entire_val:
#     print(val.text)


