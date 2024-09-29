# service analyzer file
# service_analyzer.py
import pandas as pd

def analyze_services(filename='services_data.csv'):
    # Load services data
    services_data = pd.read_csv(filename)
    
    # Example analysis: count services per category and assign a saturation score
    service_counts = services_data.groupby('title').size()
    max_services = service_counts.max()
    
    services_data['saturation_score'] = services_data['title'].map(lambda title: service_counts[title] / max_services)
    
    return services_data

if __name__ == '__main__':
    analyzed_data = analyze_services()
    print(analyzed_data)
