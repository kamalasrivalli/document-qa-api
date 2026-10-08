from app.database.connection import get_connection


def get_all_documents():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM documents")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def create_document(name: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO documents (name) VALUES (%s) RETURNING id, name",
        (name,)
    )

    new_document = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    return new_document

def get_document_by_id(document_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name FROM documents WHERE id = %s",
        (document_id,)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1]
    }

def update_document(document_id: int, name: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE documents
        SET name = %s
        WHERE id = %s
        RETURNING id, name
        """,
        (name, document_id)
    )

    row = cursor.fetchone()

    if row is None:
        cursor.close()
        conn.close()
        return None

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "id": row[0],
        "name": row[1]
    }

def delete_document(document_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM documents WHERE id = %s RETURNING id, name",
        (document_id,)
    )

    row = cursor.fetchone()

    if row is None:
        cursor.close()
        conn.close()
        return None

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Document deleted",
        "document": {
            "id": row[0],
            "name": row[1]
        }
    }