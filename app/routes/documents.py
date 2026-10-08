from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.document_service import get_all_documents, update_document
from app.services.document_service import create_document
from app.services.document_service import get_document_by_id
from app.services.document_service import delete_document

from app.database.connection import get_connection

class Document(BaseModel):
    name: str

class DocumentResponse(BaseModel):
    id: int
    name: str

class DeleteResponse(BaseModel):
    message: str
    document: DocumentResponse


router = APIRouter()

documents = [
    {
        "id": 1,
        "name": "telugu_thesis.pdf"
    },
    {
        "id": 2,
        "name": "morphology_notes.pdf"
    }
]

@router.get("/documents", response_model=list[DocumentResponse])
def get_documents():
    rows = get_all_documents()

    return [
    {"id": row[0], "name": row[1]}
    for row in rows
]


@router.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int):
    document = get_document_by_id(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document

@router.post("/documents", response_model=DocumentResponse)
def create_document_route(document: Document):
    new_document = create_document(document.name)

    return {
        "id": new_document[0],
        "name": new_document[1]
    }

@router.delete("/documents/{document_id}", response_model=DeleteResponse)
def delete_document_route(document_id: int):

    deleted_document = delete_document(document_id)

    if deleted_document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )


    return deleted_document

@router.put("/documents/{document_id}", response_model=DocumentResponse)
def update_document_route(document_id: int, document: Document):
    updated_document = update_document(document_id, document.name)
    if updated_document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return updated_document