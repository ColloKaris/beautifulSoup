from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Ask users how many times they want to click on the load more button.
# Convert the result of input() to an integer
number_of_clicks = int(input("Input the number of times you want to click on the 'Load more' button and press ENTER\n"))

# Browser initialization
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the webpage
url = 'https://www.scrapingcourse.com/button-click'
driver.get(url)

# Click on the load more button the specified number of times
for i in range(number_of_clicks):
    # Wait until the Load more button appears.
  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "load-more-btn")))

  # Locate and retrieve the load more button
  load_more_button = driver.find_element(By.ID, 'load-more-btn')

  # Click on the load more button
  load_more_button.click()

  #add a small delay to mimic human behavior
  time.sleep(2)

# fetch all products based on their class name
all_products = driver.find_elements(By.CLASS_NAME, 'product-item')
list_of_products = [] # empty list to hold all products

# logic to retrieve product details
for product in all_products:
  # product name
  name_element = product.find_element(By.CLASS_NAME, 'product-name')
  product_name = name_element.text
  
  # Product Price
  price_element = product.find_element(By.CLASS_NAME, 'product-price')
  product_price = price_element.text
  
  # Image link
  img_element = product.find_element(By.TAG_NAME, 'img')
  image_link = img_element.get_attribute('src')
  
  # Product Url
  product_url_element = product.find_element(By.TAG_NAME, 'a')
  product_url = product_url_element.get_attribute('href')
  
  # Put all product details in a dictionary
  single_product = {'Name': product_name, 'Price': product_price,
                    'Image link': image_link, 'Product URL': product_url}
  
  # Add the single_product dictionary into the list_of_products
  list_of_products.append(single_product)

print(f'You fetched {len(list_of_products)} products from the page')
# print(list_of_products)

# Export the extracted list to a CSV file.
# Specify the name of the csv file to write into.
filename = 'products.csv' 

# Open the csv file in write mode
with open(filename, 'w', newline='') as file:
  
  # Create a DictWriter object to write a dictionary to a CSV file.
  writer = csv.DictWriter(file, fieldnames=list_of_products[0].keys())

  # Write the column names for the csv file.
  writer.writeheader()

  # Write the dictionaries as rows in the csv file.
  writer.writerows(list_of_products)

print(f'The list has been written to {filename}')

# Close the browser and end the WebDriver session
driver.quit()