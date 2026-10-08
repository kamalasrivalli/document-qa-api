import psycopg

conn = psycopg.connect(
    "dbname=document_qa"
)

print("Database connection successful!")

conn.close()