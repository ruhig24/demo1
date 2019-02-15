from selenium import webdriver

browser='chrome'

if browser=='chrome':
    driver=webdriver.Chrome()
# elif browser=='ff':
#     driver=webdriver.Firefox(executable_path="")
elif browser=='ie':
    driver=webdriver.Ie(executable_path="C:/Users/ruhi.shrivastava/Downloads/drivers/IEDriverServer.exe")
driver.get("http://facebook.com")
driver.maximize_window()