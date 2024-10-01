import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import logging
import traceback
import time

# Set up logging
logging.basicConfig(level=logging.INFO)

# List of different User-Agent strings to rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

# List of proxy servers (if available) to rotate
PROXIES = [
    # 'http://87.247.186.40:1081',   # United Arab Emirates
    # 'http://222.108.214.168:8080',
    'http://81.12.104.36:3629',
#     'http://45.227.92.213:8080',
#     'http://180.183.13.200:5678',
]

# Accept-Language header values to rotate
ACCEPT_LANGUAGES = [
    "en-US,en;q=0.9",
    "en-GB,en;q=0.9",
    "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
    "es-ES,es;q=0.9,en;q=0.7"
]

# Referer values to simulate different browsing origins
REFERERS = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://duckduckgo.com/"
]

# To track already used proxies and user agents
used_user_agents = []
used_proxies = []

def get_random_user_agent():
    global used_user_agents
    if len(used_user_agents) == len(USER_AGENTS):
        # If all user agents are used, reset the list
        used_user_agents = []
    available_agents = list(set(USER_AGENTS) - set(used_user_agents))
    user_agent = random.choice(available_agents)
    used_user_agents.append(user_agent)
    return user_agent

def get_random_proxy():
    global used_proxies
    if len(used_proxies) == len(PROXIES):
        # If all proxies are used, reset the list
        used_proxies = []
    available_proxies = list(set(PROXIES) - set(used_proxies))
    proxy = random.choice(available_proxies)
    used_proxies.append(proxy)
    return proxy

def get_random_accept_language():
    return random.choice(ACCEPT_LANGUAGES)

def get_random_referer():
    return random.choice(REFERERS)

def scrape_category():
    # Setting Chrome options
    options = Options()
    # Run in visible (non-headless) mode to avoid anti-bot detection
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("start-maximized")

    # Use a random user-agent
    user_agent = get_random_user_agent()
    options.add_argument(f"user-agent={user_agent}")
    logging.info(f"Using User-Agent: {user_agent}")

    # Optionally add a random proxy
    proxy = get_random_proxy()
    options.add_argument(f'--proxy-server={proxy}')
    logging.info(f"Using Proxy: {proxy}")

    # Create a dictionary with additional human-like headers
    headers = {
        "User-Agent": user_agent,
        "Accept-Language": get_random_accept_language(),
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": get_random_referer(),
        "DNT": "1",  # Do Not Track header
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "no-cache"
    }
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Navigating to Fiverr categories page
        driver.get('https://www.fiverr.com/categories')

        # Random delay to mimic human behavior
        time.sleep(random.uniform(5, 10))

        # Wait for the category elements to be present
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'sitemap-box'))
        )

        # Parse page using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        logging.info("Page loaded successfully.")

        # Scraping the categories
        categories = soup.find_all('div', class_='sitemap-box')
        for category in categories:
            category_name = category.find('h3').text.strip() if category.find('h3') else 'N/A'
            category_link = category.find('a')['href'] if category.find('a') else 'N/A'
            logging.info(f"Category: {category_name}, Link: {category_link}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        logging.error(traceback.format_exc())
    finally:
        driver.quit()



scrape_category()
print(used_proxies)
