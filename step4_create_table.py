import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('business_data.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        title TEXT NOT NULL,
        body TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

print("Table 'posts' created successfully!")

# Show table structure
cursor.execute("PRAGMA table_info(posts)")
print("\nTable Structure:")
for column in cursor.fetchall():
    print(column)

conn.commit()
conn.close()
