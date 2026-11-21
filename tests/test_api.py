from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_query_flow_and_caching():
    # 1. First execution (Cache miss)
    resp1 = client.post("/api/v1/query", json={"query": "What is the transactional outbox SLA?"})
    assert resp1.status_code == 200
    data1 = resp1.json()
    assert data1["cached"] is False
    assert data1["routed_agent"] == "doc_agent"

    # 2. Second execution (Cache hit)
    resp2 = client.post("/api/v1/query", json={"query": "What is the transactional outbox SLA?"})
    assert resp2.status_code == 200
    data2 = resp2.json()
    assert data2["cached"] is True
    assert "Semantic Cache Hit" in data2["answer"]
