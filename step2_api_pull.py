import requests

# Define the endpoint
#url = "https://jsonplaceholder.typicode.com/posts"
url = "https://jsonplaceholder.typicode.com/posts?userId=1"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()          # Convert JSON response to Python list/dict
    print(f"Successfully retrieved {len(data)} records.")
    print("\nFirst record preview:")
    print(data[0])                  # Show the first item
else:
    print(f"Failed. Status code: {response.status_code}")
