from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="watch"

for i in range(1,5):
    driver.get(f"https://www.vardiano.com/search-results?q={query}&type=products&page={i}")

    elems = driver.find_elements(By.CLASS_NAME, "sERPSMg")
    print(f"{len(elems)} items found")
    print(elems)
    for elem in elems:
        print(elem.text)

    #print(elem.get_attribute("outerHTML"))

    time.sleep(4)
    driver.close()

