from sre_compile import isstring
from tokenize import String
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from openpyxl import Workbook,load_workbook

import time
import re

def dog_item_collector(url):

    return_row = []

    return_row.append(url)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    time.sleep(2)

    # 1. Get product name
    titleElem = driver.find_element(
        by=By.CSS_SELECTOR, value='h1[class*="u-h3"]')
    # name = titleElem.text.replace(",", "_")
    name = titleElem.text
    return_row.append(name)

    # 1.1 Get images
    imageElem = driver.find_element(
        by=By.CSS_SELECTOR, value='li[class*="_styledimage-slider"] div div')
    url = imageElem.value_of_css_property('background-image')[5::1][:-2:1]
    return_row.append(url)

    # 2. Get product price
    priceElem = driver.find_element(
        by=By.CSS_SELECTOR, value='div[class*="_styledprices__PDPPriceItems"]')
    price = priceElem.text.splitlines(
    )[2] + '.' + priceElem.text.splitlines()[3]
    return_row.append(price)

    # 3. Get Description
    descriptionElem = driver.find_element(
        by=By.CSS_SELECTOR, value='li[data-product-details*="Description"]')
    description = descriptionElem.text

    descriptionElem.click()
    time.sleep(1)

    descriptionDesc = driver.find_element(
        by=By.CSS_SELECTOR, value='div[class*="_styledproduct-info__Description"]')
    # desc = descriptionDesc.text.replace(",", "_")
    desc = descriptionDesc.text
    return_row.append(desc)

    # 4. Get Ingredients
    ingredientsElem = driver.find_element(
        by=By.CSS_SELECTOR, value='li[data-product-details*="Ingredients"]')
    ingredients = ingredientsElem.text

    ingredientsElem.click()
    time.sleep(1)

    ingredientsDesc = driver.find_element(
        by=By.CSS_SELECTOR, value='div[class*="_styledproduct-info__Description"]')
    # ingred = ingredientsDesc.text.replace(",", "_")
    ingred = ingredientsDesc.text
    return_row.append(ingred)

    # 5. Get Specifications & Guides
    specificationsGuidesElem = driver.find_element(
        by=By.CSS_SELECTOR, value='li[data-product-details*="Specifications & Guides"]')
    specificationsGuides = specificationsGuidesElem.text

    specificationsGuidesElem.click()
    time.sleep(1)

    specificationsGuidesDesc = driver.find_element(
        by=By.CSS_SELECTOR, value='div[class*="_styledproduct-info__Description"]')
    # spec = specificationsGuidesDesc.text.replace(",", "_")
    spec = specificationsGuidesDesc.text
    return_row.append(spec)

    driver.close()

    return return_row

def dog_master_collector(url):
    # dog has 77 pages
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    time.sleep(5)

    # Get item list
    ele = driver.find_elements_by_xpath('//*/a')

    itemList = []
    for x in ele:
        href = x.get_attribute("href")

        if(isstring(href)):
            if "/products" in href:
                itemList.append(str(href))

    itemList = list(set(itemList))
    driver.close()

    return itemList

def write_data_to_xlsx(url, filename, sheetname):
    # url = "https://www.petstock.com.au/products/supercoat-smartblend-large-breed-adult-chicken-dry-dog-food-1"
    row_contents = dog_item_collector(url)

    # save data to 
    # Start by opening the spreadsheet and selecting the main sheet
    workbook = load_workbook(filename=filename)
    worksheet = workbook[sheetname]

    # Write what you want into a specific cell
    worksheet.append(row_contents)

    # Save the spreadsheet
    workbook.save(filename=filename)

