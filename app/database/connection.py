import psycopg


def get_connection():
    return psycopg.connect(
        "dbname=document_qa"
    )