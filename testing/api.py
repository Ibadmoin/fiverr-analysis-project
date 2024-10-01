from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
import random


def scrape_categories():
    # Configure Selenium with dynamic headers
    chrome_options = Options()
    
    # List of User-Agents
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 11; Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36"
        # Add more User-Agents as needed
    ]
    
    # Randomly choose a User-Agent
    user_agent = random.choice(user_agents)
    chrome_options.add_argument(f"user-agent={user_agent}")
    
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.fiverr.com/categories")
    
    # Wait for dynamic content to load
    time.sleep(random.uniform(3, 6))  # Random delay between 3 to 6 seconds
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'sitemap')))
    
    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    print(soup.prettify())
    categories = []

    # Main category elements
    # main_categories = soup.find_all('div', class_='sitemap-box')  # Example selector
    

    # for main_category in main_categories:
    #     category_name = main_category.find('h5').text.strip()  # Main category name
        
    #     # Find all subcategories within the main category
    #     subcategories = main_category.find_all('a', class_='subcategory-link')  # Example selector
        
    #     for subcategory in subcategories:
    #         subcategory_name = subcategory.text.strip()
    #         subcategory_url = subcategory['href']
    #         categories.append({
    #             'main_category': category_name,
    #             'subcategory': subcategory_name,
    #             'url': subcategory_url
    #         })
    
    # return categories

def save_to_csv(categories, filename='categories.csv'):
    # Save the category and subcategory data to CSV
    keys = categories[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(categories)

if __name__ == '__main__':
    categories = scrape_categories()
    save_to_csv(categories)
    print(categories)
