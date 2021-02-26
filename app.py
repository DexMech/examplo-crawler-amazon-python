from selenium import webdriver
import time
from bs4 import BeautifulSoup

header='Nome\tPreço\n'

driver = webdriver.Chrome()
driver.get("https://amazon.com.br")
 
element = driver.find_element_by_id("twotabsearchtextbox")
element.send_keys('iphone')
element.submit()
time.sleep(5)

htmlElement = driver.find_element_by_tag_name("html")
htmlText = htmlElement.get_attribute("innerHTML")
soup = BeautifulSoup(htmlText, "html.parser")

phones = soup.select(".a-section.a-spacing-medium")
xlsx = open('file.xlsx','w')
xlsx.write(header)
for phone in phones:
    price = ''
    name = ''
    priceElement = phone.select_one(".a-price-whole")
    nameElement = phone.select_one(".a-size-base-plus.a-color-base.a-text-normal")
    if nameElement != None:
        name = nameElement.text.replace(',', '')
        if priceElement != None:
            price = priceElement.text.replace(',', '')
            xlsx.write(name + "\tR$" + price + "\n")

xlsx.close()
driver.close()