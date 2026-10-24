from fastapi import FastAPI
from app.routes.questions import router as question_router
from app.routes.documents import router as document_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Document Q&A API is running - CI/CD verified"}


app.include_router(question_router)
app.include_router(document_router)
