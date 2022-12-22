import requests
from bs4 import BeautifulSoup
import openpyxl

# Set the URL of the website to scrape
url = 'https://www.karaca.com/halilar'

# Make a request to the website and retrieve the HTML
response = requests.get(url)
html = response.text

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the product information in the HTML using the soup object's methods
products = soup.find_all('div', class_='productWrap')

# Create a new Excel workbook and add a sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add headers to the sheet
sheet.append(['Name', 'Price', 'Information', 'Tags'])

# Iterate over the products and write their information to the sheet
for product in products:
    tilt = product.find('span', class_='title').text.replace('\n', '')
    price = product.find('span', class_='prices').text.replace('\n', '')
    sheet.append([tilt, price])

# Save the workbook
workbook.save('products.xlsx')
