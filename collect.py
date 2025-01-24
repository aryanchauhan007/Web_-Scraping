from bs4 import BeautifulSoup
import os
import pandas as pd
d = {'title': [], 'price':[], 'link':[]}
for file in os.listdir("data"):
  try: 
    with open(f"data/{file}") as f:
     html_doc=f.read()
    soup = BeautifulSoup(html_doc, 'html.parser') 
    t= soup.find(class_="sJpr9vC")
    title= t.get_text()

    p = soup.find(class_="sQq4biu")
    price= p.get_text()

    l = t.find("a")
    link = l['href']
  
    print(title, price, link)
    d['title'].append(title)
    d['price'].append(price)
    d['link'].append(link)
  except Exception as e:
    print(e)


df =pd.DataFrame(data=d)    
df.to_csv("data.csv")


 
