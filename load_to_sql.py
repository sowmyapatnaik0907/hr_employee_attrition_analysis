
import pandas as pd
import sqlite3
import os

# ====================================
# HR ATTRITION - SQL DATABASE CREATION
# ====================================

# Load cleaned dataset
df = pd.read_csv("hr_attrition_cleaned.csv")

print("Dataset loaded successfully!")

# Create SQLite database
connection = sqlite3.connect("hr_attrition.db")

# Import dataset into SQL table
df.to_sql(
    "employee_attrition",
    connection,
    if_exists="replace",
    index=False
)

print("Dataset imported into SQL successfully!")

# Verify employee records
cursor = connection.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM employee_attrition"
)

total_records = cursor.fetchone()[0]

print("\nSQL DATABASE DETAILS")
print("----------------------------")

print("Database Name: hr_attrition.db")
print("Table Name: employee_attrition")
print("Total Records:", total_records)

# Display first 5 records
print("\nFIRST 5 RECORDS FROM SQL")

cursor.execute(
    "SELECT * FROM employee_attrition LIMIT 5"
)

records = cursor.fetchall()

for record in records:
    print(record)

connection.close()

print("\nSQL DATABASE CREATED SUCCESSFULLY!")


