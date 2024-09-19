# Web Scraper for Newegg Products

This is a Python web scraper built using BeautifulSoup and the requests library. The scraper allows users to search for products on Newegg, extract the product name, price, and product link for each item, and display them in the console.

## Features:
- Search for products on Newegg.ca by a specific term.
- Scrape product information including:
  - Product Name
  - Price
  - Product Link
- Display results in the console.

## Requirements:

Make sure you have Python installed. You will also need the following Python packages:
- **BeautifulSoup**: For parsing HTML data.
- **requests**: For making HTTP requests.
- **re**: (built-in) for handling regular expressions to extract prices.

You can install the required libraries using pip:

```bash
pip install beautifulsoup4 requests
