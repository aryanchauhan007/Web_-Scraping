from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="watch"
file = 0
for i in range(1,4):
    driver.get(f"https://www.vardiano.com/search-results?q={query}&type=products&page={i}")

    elems = driver.find_elements(By.CLASS_NAME, "sERPSMg")
    print(f"{len(elems)} items found")
    
    for elem in elems:
         d = elem.get_attribute("outerHTML")
         with open(f"data/{query}_{file}.html" , "w", encoding="UTF-8") as f:
              f.write(d)
              file += 1
        #print(elem.text)

    #print(elem.get_attribute("outerHTML"))

    time.sleep(4)
driver.close()

