
import sqlite3

# Connect to existing database
connection = sqlite3.connect("hr_attrition.db")

# Read SQL file
with open("attrition_analysis.sql", "r") as file:
    sql_queries = file.read()

# Execute individual SQL queries
cursor = connection.cursor()

queries = sql_queries.split(";")

for query in queries:

    if query.strip():

        cursor.execute(query)

        if cursor.description:

            print("\n" + "=" * 55)
            print("QUERY RESULT")
            print("=" * 55)

            columns = [column[0] for column in cursor.description]

            print(" | ".join(columns))

            for row in cursor.fetchall():
                print(row)

connection.close()

print("\nALL SQL QUERIES EXECUTED SUCCESSFULLY!")
