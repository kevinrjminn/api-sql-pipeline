import requests
import sqlite3
from datetime import datetime

# 1. Pull data from API
url = "https://jsonplaceholder.typicode.com/posts?userId=1"
response = requests.get(url)

if response.status_code != 200:
    print(f"API request failed: {response.status_code}")
    exit()

data = response.json()

# 2. Connect to database
conn = sqlite3.connect('business_data.db')
cursor = conn.cursor()

# 3. Insert each record
inserted_count = 0
for post in data:
    try:
        cursor.execute('''
            INSERT INTO posts (user_id, title, body)
            VALUES (?, ?, ?)
        ''', (post['userId'], post['title'], post['body']))
        inserted_count += 1
    except Exception as e:
        print(f"Error inserting record {post.get('id')}: {e}")

conn.commit()
conn.close()

print(f"Successfully inserted {inserted_count} records into the database.")
