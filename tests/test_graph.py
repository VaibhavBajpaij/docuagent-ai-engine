from src.agents.graph import LangGraphOrchestrator

def test_langgraph_doc_routing():
    orchestrator = LangGraphOrchestrator()
    res = orchestrator.run("What is the transactional outbox pattern in Kafka?")
    assert res["routed_agent"] == "doc_agent"
    assert "transactional outbox" in res["answer"].lower()
    assert res["confidence"] > 0.5
    assert len(res["sources"]) > 0
    assert any("EvidenceGrounder" in step for step in res["trace"])

def test_langgraph_sql_analytics_routing():
    orchestrator = LangGraphOrchestrator()
    res = orchestrator.run("How many failed transactions occurred in the ledger?")
    assert res["routed_agent"] == "sql_agent"
    assert "SQL Analytics Report" in res["answer"]
    assert "FAILED" in res["answer"]
    assert res["confidence"] == 0.98
    assert len(res["sources"]) > 0
