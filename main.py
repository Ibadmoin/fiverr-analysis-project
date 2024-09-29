# main python files to call module functions

# main.py
from scraper.service_scraper import scrape_services, save_services_to_csv
from analysis.service_analyzer import analyze_services
from analysis.opportunity_finder import find_opportunities
from models.llm_model import get_service_suggestions
from scheduler.schedule_scrape import job

def main():
    print("Starting the Fiverr Analysis Project")
    
    # Step 1: Scrape services
    category_url = "https://www.fiverr.com/categories/design/graphics-logo-design"
    services = scrape_services(category_url)
    save_services_to_csv(services)
    
    # Step 2: Analyze services
    analyzed_services = analyze_services()
    print("Analyzed Services:", analyzed_services)
    
    # Step 3: Identify opportunities
    opportunities = find_opportunities(analyzed_services)
    print("Opportunities:", opportunities)
    
    # Step 4: Generate LLM suggestions for new services
    subcategory = "logo design"
    suggestions = get_service_suggestions(subcategory)
    print("Service Suggestions:", suggestions)

if __name__ == '__main__':
    main()
