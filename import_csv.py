import sqlite3
import csv

# Database Connect
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Delete old table
cursor.execute("DROP TABLE IF EXISTS numbers")

# Create new table
cursor.execute("""
CREATE TABLE numbers (
    DE_ID TEXT
)
""")

# Fast Search Index
cursor.execute("""
CREATE INDEX idx_deid
ON numbers(DE_ID)
""")

# Read CSV
with open("csv/data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    data = [(row[0],) for row in reader if row]

# Insert Data
cursor.executemany(
    "INSERT INTO numbers (DE_ID) VALUES (?)",
    data
)

conn.commit()
conn.close()

print(f"✅ Imported {len(data)} records successfully.")