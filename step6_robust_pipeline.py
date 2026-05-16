import requests
import sqlite3
import logging
from datetime import datetime

# === Setup Logging ===
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("=== Starting API to SQL Pipeline ===")

# 1. Pull data from API
url = "https://jsonplaceholder.typicode.com/posts?userId=1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()          # Raises error for bad status codes
    
    data = response.json()
    logging.info(f"Successfully retrieved {len(data)} records from API")
    
except requests.exceptions.Timeout:
    logging.error("API request timed out")
    exit(1)
except requests.exceptions.RequestException as e:
    logging.error(f"API request failed: {e}")
    exit(1)

# 2. Connect to database
try:
    conn = sqlite3.connect('business_data.db')
    cursor = conn.cursor()
    
    inserted_count = 0
    skipped_count = 0
    
    for post in data:
        try:
            cursor.execute('''
                INSERT INTO posts (user_id, title, body)
                VALUES (?, ?, ?)
            ''', (post['userId'], post['title'], post['body']))
            inserted_count += 1
            
        except sqlite3.IntegrityError:
            skipped_count += 1
            logging.warning(f"Duplicate record skipped (id: {post.get('id')})")
        except Exception as e:
            logging.error(f"Failed to insert record {post.get('id')}: {e}")
    
    conn.commit()
    logging.info(f"Insertion complete. Inserted: {inserted_count}, Skipped: {skipped_count}")

except Exception as e:
    logging.error(f"Database error: {e}")
    exit(1)
finally:
    conn.close()

logging.info("=== Pipeline finished successfully ===\n")
print(f"Pipeline completed. Inserted {inserted_count} records. Check pipeline.log for details.")
