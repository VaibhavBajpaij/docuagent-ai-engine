from src.agents.router import AgentRouter

def test_agent_router_sql_queries():
    assert AgentRouter.route_query("What is the total sum of payments?") == "sql_agent"
    assert AgentRouter.route_query("How many rows in transactions table?") == "sql_agent"

def test_agent_router_web_queries():
    assert AgentRouter.route_query("What is the latest stock price today?") == "web_search_agent"

def test_agent_router_doc_queries():
    assert AgentRouter.route_query("Explain the transactional outbox pattern") == "doc_agent"
