from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

import re

pattern = re.compile(r"^_styledproduct-info")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.petstock.com.au/products/ziwipeak-daily-dog-cuisine-chicken-wet-dog-food")

# 1. Get product name
titleElem = driver.find_element(by=By.CSS_SELECTOR, value='h1[class*="u-h3"]')
print(titleElem.text)


# 1.1 Get images
imageElem = driver.find_element(by=By.CSS_SELECTOR, value='li[class*="_styledimage-slider"] div div')
url = imageElem.value_of_css_property('background-image')[5::1][:-2:1]
print(url)

# 2. Get product price
priceElem = driver.find_element(by=By.CSS_SELECTOR, value='div[class*="_styledprices__PDPPriceItems"]')
price =  priceElem.text.splitlines()[2] + '.' + priceElem.text.splitlines()[3]
print(price)

# 3. Get Description
print("------------")
descriptionElem = driver.find_element(by=By.CSS_SELECTOR, value='li[data-product-details*="Description"]')
description = descriptionElem.text
print(description)

descriptionDesc = driver.find_element(by=By.CSS_SELECTOR, value='div[class*="_styledproduct-info__Description"]')
print(descriptionDesc.text)


# 4. Get Ingredients
print("------------")
ingredientsElem = driver.find_element(by=By.CSS_SELECTOR, value='li[data-product-details*="Ingredients"]')
ingredients = ingredientsElem.text
print(ingredients)

ingredientsElem.click()
time.sleep(1)

ingredientsDesc = driver.find_element(by=By.CSS_SELECTOR, value='div[class*="_styledproduct-info__Description"]')
print(ingredientsDesc.text)

# 5. Get Specifications & Guides
print("------------")
pecificationsGuidesElem = driver.find_element(by=By.CSS_SELECTOR, value='li[data-product-details*="Specifications & Guides"]')
specificationsGuides = pecificationsGuidesElem.text
print(specificationsGuides)

pecificationsGuidesElem.click()
time.sleep(1)

specificationsGuidesDesc = driver.find_element(by=By.CSS_SELECTOR, value='div[class*="_styledproduct-info__Description"]')
print(specificationsGuidesDesc.text)

# 6. Get Reviews
# print("------------")
# reviewsElem = driver.find_element(by=By.CSS_SELECTOR, value='li[data-product-details*="Reviews"]')
# reviews = reviewsElem.text
# print(reviews)

# reviewsElem.click()
# time.sleep(1)

# reviewsDesc = driver.find_element(by=By.CSS_SELECTOR, value='div[class*="_styledproduct-info__Description"]')
# print(reviewsDesc.text)




# for element in elements:
#     match = pattern.match(element.text)
#     if match:
#         print(element.text)

# for link in all_links:
#     print(link.text)

driver.close()