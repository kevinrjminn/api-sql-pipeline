import requests
import sqlite3
import logging
from datetime import datetime

# === Logging Setup ===
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("=== Starting Automated API → SQL Pipeline ===")

try:
    # 1. API Call
    url = "https://jsonplaceholder.typicode.com/posts?userId=1"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    
    data = response.json()
    logging.info(f"Retrieved {len(data)} records from API")

    # 2. Database Insert
    conn = sqlite3.connect('business_data.db')
    cursor = conn.cursor()
    
    inserted = 0
    skipped = 0
    
    for post in data:
        try:
            cursor.execute('''
                INSERT INTO posts (user_id, title, body)
                VALUES (?, ?, ?)
            ''', (post['userId'], post['title'], post['body']))
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1
        except Exception as e:
            logging.error(f"Insert error for record {post.get('id')}: {e}")
    
    conn.commit()
    logging.info(f"Completed: {inserted} inserted, {skipped} skipped")

except requests.exceptions.RequestException as e:
    logging.error(f"API Error: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
finally:
    if 'conn' in locals():
        conn.close()

logging.info("=== Pipeline finished ===\n")
print("Automated pipeline executed successfully.")
