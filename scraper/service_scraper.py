# service scraper file

# service_scraper.py
import requests
from bs4 import BeautifulSoup
import csv

def scrape_services(category_url):
    # Send request to category page
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract service details from page (you'll need to adjust the logic based on the actual Fiverr structure)
    services = []
    for service in soup.find_all('div', class_='service-tile'):
        title = service.find('h3').text
        reviews = service.find('span', class_='review-count').text
        price = service.find('span', class_='service-price').text
        services.append({'title': title, 'reviews': reviews, 'price': price})
    
    return services

def save_services_to_csv(services, filename='services_data.csv'):
    # Save scraped data to CSV
    keys = services[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(services)

if __name__ == '__main__':
    category_url = "https://www.fiverr.com/categories/design/graphics-logo-design"
    services = scrape_services(category_url)
    save_services_to_csv(services)
