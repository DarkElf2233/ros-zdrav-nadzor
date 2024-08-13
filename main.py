from selenium import webdriver
from selenium.webdriver.common.by import By

import sys
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://roszdravnadzor.gov.ru/services/mi_reesetr")

try:
    tr = driver.find_element(By.CLASS_NAME, "odd")
except:
    driver.close()
    sys.exit()

btn = driver.find_element(By.CLASS_NAME, "ico-xls")
btn.click()

time.sleep(3 * 60)

driver.close()
