# scheduler scrape file

# schedule_scrape.py
import schedule
import time
from scraper.service_scraper import scrape_services, save_services_to_csv

def job():
    print("Scraping services...")
    category_url = "https://www.fiverr.com/categories/design/graphics-logo-design"
    services = scrape_services(category_url)
    save_services_to_csv(services)

# Schedule the scraping job daily/weekly/monthly
schedule.every().day.at("10:00").do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
