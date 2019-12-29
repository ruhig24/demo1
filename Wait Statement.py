from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.google.co.in")
driver.maximize_window()

# element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gsr")))
# print("program executed1")
#
# e1=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"ei")))
# # WebDriverWait(driver,10).until(EC.title_is,"Search")
# try:
#     WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"q")))
#     print("program executed")
# except Exception:
#     print("failed execution")
# finally:
#     driver.quit()


# WebDriverWait(driver,10).until(EC.title_contains,"ggfcg") Need to check
# WebDriverWait(driver,10).until(EC.element_to_be_clickable)
#
# print("program executed")



