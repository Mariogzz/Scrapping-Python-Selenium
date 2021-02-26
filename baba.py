import wget
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

#driver =webdriver.Chrome()

driver.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=riot+gear")
time.sleep(1)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

items = driver.find_elements_by_css_selector(".J-offer-wrapper")

output = []

for i in items:

    try:
        product_name = i.find_element_by_css_selector("h4").text
    except:
        product_name = None
   
    try:
        price = i.find_element_by_css_selector(".elements-offer-price-normal").text
    except:
        price = None
    
    #try:
    #    img_div = i.find_element_by_css_selector("seb-img-switcher__imgs")
    #    img_url = img_div.get_attribute("data-image")
    #    img_url = "https:" + img_url
    #    img_url = img_url.replace("_300x300.jpg","")
    #    img_url = img_url.replace("_300x300.png","")
    #    destination = "images/" + img_url.split("/")[-1]
    #    wget.download(img_url, destination)
    #except:
    #    img_url = None
    
    output_item = {
    #    "img" : img_url,
        "price" : price,
        "product_name" : product_name
    }

    output.append(output_item)

    # print(price, product_name, img_url)

json.dump(output, open("product.json","w"), indent=2)
driver.close()