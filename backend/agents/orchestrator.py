class Orchestrator:
    def __init__(self, data_agent=None, research_agent=None):
        self.data_agent = data_agent
        self.research_agent = research_agent

    def route(self, query: str):
        query_lower = query.lower()

        # If both agents exist, try to detect based on keywords
        if self.data_agent and self.research_agent:
            if any(word in query_lower for word in ["sales", "revenue", "trend", "product", "data", "csv", "table"]):
                return self.data_agent.handle(query)
            elif any(word in query_lower for word in ["paper", "summarize", "research", "keywords", "pdf"]):
                return self.research_agent.handle(query)
            else:
                # Default: return both results
                return {
                    "data_agent": self.data_agent.handle(query),
                    "research_agent": self.research_agent.handle(query)
                }

        # Only data agent exists
        if self.data_agent:
            return self.data_agent.handle(query)

        # Only research agent exists
        if self.research_agent:
            return self.research_agent.handle(query)

        return "No agent is available. Please upload a CSV or PDF."
