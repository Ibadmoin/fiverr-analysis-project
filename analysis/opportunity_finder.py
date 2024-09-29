# opportunity finder file
# opportunity_finder.py
import pandas as pd

def load_services_data(filename='services_data.csv'):
    # Load the scraped services data from CSV
    return pd.read_csv(filename)

def find_opportunities(services_data):
    # Analyze services to identify underserved segments
    # Example logic: if a segment has fewer than 10 providers and high demand, it's underserved
    underserved = services_data[services_data['reviews'].astype(int) < 10]
    return underserved

if __name__ == '__main__':
    services_data = load_services_data()
    opportunities = find_opportunities(services_data)
    print(opportunities)
