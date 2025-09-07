from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

import csv

from dotenv import load_dotenv

import os

load_dotenv()

driver_option = webdriver.ChromeOptions()
driver_option.add_argument('--incognito')

chromedriver_path = os.getenv('CHROMEDRIVER-PATH')

def create_webdriver():
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)

def scrape_url(url):
    product_list = {}
    browser = create_webdriver()
    browser.get(url)
    
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-wrapper card-body']")))
    
    products = browser.find_elements(By.XPATH, "//div[@class='product-wrapper card-body']")
    
    for product in products:
        try:
            product_name = product.find_element(By.TAG_NAME, "a").text
            product_url = product.find_element(By.TAG_NAME, "a").get_attribute('href')
            product_desc = product.find_element(By.TAG_NAME, "p").text
            product_price = product.find_element(By.TAG_NAME, "span").text
            product_review = product.find_element(By.XPATH, ".//span[@itemprop='reviewCount']").text
            product_list[product_name] = [product_url, product_desc, product_price, product_review]
        except NoSuchElementException:
            # Caso algum elemento não seja encontrado, ignore este produto
            continue
        
    browser.quit()
    return product_list

urlarray = [
    'https://webscraper.io/test-sites/e-commerce/allinone',
    'https://webscraper.io/test-sites/e-commerce/allinone/computers',
    'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops',
    'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets',
    'https://webscraper.io/test-sites/e-commerce/allinone/phones',
    'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
]

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_results = {executor.submit(scrape_url, url) for url in urlarray}

    results = []

    for future in concurrent.futures.as_completed(future_results):
        results.append(future.result())

    combined_results = {}

    for d in results:
        combined_results.update(d)

    product_df = pd.DataFrame.from_dict(combined_results, orient='index', columns=[
        'product_url', 'product_desc', 'product_price', 'product_review'])

    product_df['product_name'] = product_df.index
    product_df = product_df.reset_index(drop=True)
    product_df.to_csv('product_list.csv', index=False, quoting=csv.QUOTE_ALL)
