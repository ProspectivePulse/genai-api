from pydantic import BaseModel
from typing import List

# Input schema for query requests
class QueryRequest(BaseModel):
    query: str
    
# Output schema for responses
class QueryResponse(BaseModel):
    response: str

class DocumentRequest(BaseModel):
    text: str

class DocumentResponse(BaseModel):
    message: str

class SearchResult(BaseModel):
    text: str
    score: float