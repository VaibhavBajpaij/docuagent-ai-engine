from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class QueryRequest(BaseModel):
    query: str = Field(..., example="What are the SLA terms for enterprise payment APIs?")
    session_id: Optional[str] = "default-session"
    force_refresh: Optional[bool] = False

class SourceDocument(BaseModel):
    title: str
    relevance_score: float
    snippet: str

class QueryResponse(BaseModel):
    query: str
    answer: str
    routed_agent: str
    cached: bool
    latency_ms: float
    confidence_score: float
    sources: List[SourceDocument] = []
    trace_id: str
