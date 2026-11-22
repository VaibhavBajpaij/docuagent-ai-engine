import time
import uuid
from fastapi import APIRouter
from .models import QueryRequest, QueryResponse, SourceDocument
from ..core.semantic_cache import SemanticCache
from ..agents.graph import LangGraphOrchestrator

router = APIRouter()
cache = SemanticCache(similarity_threshold=0.88)
orchestrator = LangGraphOrchestrator()

# Pre-seed semantic cache with typical enterprise queries for immediate sub-millisecond response
cache.set(
    query="Explain semantic caching",
    answer="Semantic caching evaluates dense vector cosine similarity (>= 0.88) against historical query embeddings, returning sub-50ms verified responses and cutting redundant LLM API costs by up to 95%.",
    routed_agent="doc_agent",
    sources=[
        SourceDocument(
            title="Vector Semantic Caching Specification",
            relevance_score=0.985,
            snippet="Dual-tier semantic caching evaluates dense vector cosine similarity with a threshold of 0.88."
        )
    ]
)

@router.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    start_time = time.time()
    trace_id = "trc_" + uuid.uuid4().hex[:10]

    # 1. Semantic Cache Lookup via 256-D Cosine Similarity
    if not request.force_refresh:
        cached_result = cache.get(request.query)
        if cached_result:
            latency = (time.time() - start_time) * 1000
            sim = cached_result["similarity"]
            ans = cached_result["answer"]
            return QueryResponse(
                query=request.query,
                answer=f"[Semantic Cache Hit (Cosine: {sim:.3f})]: {ans}",
                routed_agent=cached_result["routed_agent"],
                cached=True,
                latency_ms=round(latency, 2),
                confidence_score=round(sim, 3),
                sources=cached_result["sources"],
                trace_id=trace_id
            )

    # 2. Fresh Inference via LangGraph Multi-Agent Orchestrator
    result = orchestrator.run(request.query)

    # 3. Write-Through to Semantic Cache
    cache.set(
        query=request.query,
        answer=result["answer"],
        routed_agent=result["routed_agent"],
        sources=result["sources"]
    )

    latency = (time.time() - start_time) * 1000
    return QueryResponse(
        query=request.query,
        answer=result["answer"],
        routed_agent=result["routed_agent"],
        cached=False,
        latency_ms=round(latency, 2),
        confidence_score=result["confidence"],
        sources=result["sources"],
        trace_id=trace_id
    )

@router.get("/cache/stats")
async def get_cache_stats():
    return cache.get_stats()

@router.post("/cache/clear")
async def clear_cache():
    cache.clear()
    return {"status": "cleared", "active_entries": 0}
