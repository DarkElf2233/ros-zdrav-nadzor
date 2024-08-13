from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')

driver = webdriver.Chrome()  # options=options
driver.get("https://roszdravnadzor.gov.ru/services/mi_reesetr")

try:
    tr = driver.find_element(By.CLASS_NAME, "asfsfsfs")
except:
    print('Error')
    driver.close()

btn = driver.find_element(By.CLASS_NAME, "ico-xls")

driver.close()
