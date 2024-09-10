from bs4 import BeautifulSoup
import requests
import re

search_term = input("What product do you want to search for?")

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(page_text.text.split("/")[-1])
count = 0

# Regex to match float-like values
price_pattern = re.compile(r'(\d+,\d+|\d+)\.\d+')

for page in range(1, pages + 1):
  url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
  page = requests.get(url).text
  doc = BeautifulSoup(page, "html.parser")
  items = doc.find_all('div', class_='item-cell')
  
  for item in items:
    # Get the price and convert to float value
    price_container = item.find('li', class_='price-current')
    if price_container:
      price_text = price_container.text.strip()
      match = price_pattern.search(price_text)
      if match:
        price_str = match.group(0).replace(',', '')  # Remove commas from the price
        price = float(price_str)  
        #print(price)
    
    # Get product links
    link_tag = item.find('a', class_='item-title')
    if link_tag and 'href' in link_tag.attrs:
       link = link_tag['href']
       #print(link)
    
    # Get product name
    name_tag = item.find('a', class_='item-title')
    name = name_tag.text.strip() if name_tag else 'N/A'

    print(name)
    print(price)
    print(link)
    print('\n')
  