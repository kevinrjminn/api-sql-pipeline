import requests
import json  # For pretty printing

url = "https://jsonplaceholder.typicode.com/posts?userId=1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print(f"Total records retrieved: {len(data)}\n")
    
    # Pretty print the first record
    print("=== FIRST RECORD (Pretty Printed) ===")
    print(json.dumps(data[0], indent=4))
    
    # Show all keys in the record
    print("\n=== KEYS IN EACH RECORD ===")
    print(list(data[0].keys()))
    
    # Show data types
    print("\n=== DATA TYPES ===")
    for key, value in data[0].items():
        print(f"{key}: {type(value).__name__}")
        
else:
    print(f"Request failed with status: {response.status_code}")
