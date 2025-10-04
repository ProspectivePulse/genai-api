from fastapi import FastAPI
from app.models import QueryRequest, QueryResponse, DocumentRequest, DocumentResponse, SearchResult
from app.faiss_store import add_document, search

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"FAISS-based GenAI API is running!"}

    
@app.post("/add-document", response_model=DocumentResponse)
def add_doc(payload: DocumentRequest):
    add_document(payload.text)
    return DocumentResponse(message="Document added successfully!")

@app.post("/ask", response_model=list[SearchResult])
def ask_question(payload: QueryRequest):
    results = search(payload.query)
    return results