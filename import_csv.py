import sqlite3
import csv
import os

DATABASE = "database.db"
CSV_FILE = "csv/data.csv"


# =========================
# DATABASE CONNECT
# =========================

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()


# =========================
# DELETE OLD TABLE
# =========================

cursor.execute("DROP TABLE IF EXISTS numbers")


# =========================
# CREATE NEW TABLE
# =========================

cursor.execute("""
CREATE TABLE numbers (
    Mobile TEXT PRIMARY KEY,
    "Data Status" TEXT
)
""")


# =========================
# CREATE SEARCH INDEX
# =========================

cursor.execute("""
CREATE INDEX idx_mobile
ON numbers(Mobile)
""")


# =========================
# READ CSV
# =========================

with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:

    reader = csv.DictReader(file)

    data = []

    for row in reader:

        mobile = str(row.get("Mobile", "")).strip()
        status = str(row.get("Data Status", "")).strip()

        # Remove spaces
        mobile = mobile.replace(" ", "")

        # Only 10 digit mobile numbers
        if mobile.isdigit() and len(mobile) == 10:

            data.append(
                (mobile, status)
            )


# =========================
# INSERT DATA
# =========================

cursor.executemany(
    """
    INSERT OR REPLACE INTO numbers
    (Mobile, "Data Status")
    VALUES (?, ?)
    """,
    data
)


# =========================
# SAVE DATABASE
# =========================

conn.commit()
conn.close()


# =========================
# RESULT
# =========================

print("===================================")
print("Database updated successfully!")
print(f"Total records imported: {len(data)}")
print("===================================")