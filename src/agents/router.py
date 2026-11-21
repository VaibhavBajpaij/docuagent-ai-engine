from typing import Literal

AgentType = Literal["sql_agent", "doc_agent", "web_search_agent"]

class AgentRouter:
    """Determines query intent to route between specialized reasoning agents."""
    @staticmethod
    def route_query(query: str) -> AgentType:
        q = query.lower()
        if any(w in q for w in ["how many", "count", "average", "total", "sum", "table", "rows", "sql", "transactions"]):
            return "sql_agent"
        if any(w in q for w in ["latest", "news", "today", "live", "current price", "stock", "weather"]):
            return "web_search_agent"
        return "doc_agent"
