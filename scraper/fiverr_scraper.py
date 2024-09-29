# main fiver scaraper file

import requests
from bs4 import BeautifulSoup

url = 'https://www.fiverr.com/categories'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

categories = {}

# Replace with actual Fiverr category HTML structure
for category in soup.find_all('div', class_='category-class'):
    cat_name = category.find('h3').text
    subcategories = [sub.text for sub in category.find_all('a', class_='subcategory-class')]
    categories[cat_name] = subcategories

print(categories)
