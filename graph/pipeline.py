from langgraph.graph import StateGraph, START, END

from core.state import State
from agents.auditor import auditor_agent
from agents.analyst import analyst_agent

def build_pipeline(llm, retriever):
    graph = StateGraph(State)

    graph.add_node("auditor", lambda state: auditor_agent(state, llm))
    graph.add_node("analyst", lambda state: analyst_agent(state, retriever))

    graph.add_edge(START, "auditor")
    graph.add_edge("auditor", "analyst")
    graph.add_edge("analyst", END)

    return graph.compile()
