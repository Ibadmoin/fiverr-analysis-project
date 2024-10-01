import requests

# List of proxies to test
PROXIES = [
    'http://177.223.238.20:4153',
    'http://202.137.17.151:5678',
    
]

# URL to test the proxy (httpbin.org provides a simple endpoint to check IP address)
test_url = "https://www.fiverr.com"

for proxy in PROXIES:
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    try:
        print(f"Testing proxy {proxy}")
        response = requests.get(test_url, proxies=proxies, timeout=10)
        print("Success:", response.json())
    except Exception as e:
        print(f"Failed to connect with proxy {proxy}: {e}")
