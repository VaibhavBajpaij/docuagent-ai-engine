from src.core.semantic_cache import SemanticCache

def test_semantic_cache_exact_and_near_hit():
    cache = SemanticCache(similarity_threshold=0.85)
    cache.set("What is the payment API rate limit?", "500 req/sec via Redis token bucket", "doc_agent")

    # Near query
    hit = cache.get("What is the rate limit for payment API?")
    assert hit is not None
    answer, sim, agent = hit
    assert "500 req/sec" in answer
    assert sim >= 0.85

def test_semantic_cache_miss_on_unrelated_query():
    cache = SemanticCache(similarity_threshold=0.90)
    cache.set("What is the payment API SLA?", "99.99% uptime", "doc_agent")

    hit = cache.get("How to bake chocolate cookies?")
    assert hit is None
