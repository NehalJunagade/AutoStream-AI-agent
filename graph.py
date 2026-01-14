from langgraph.graph import StateGraph, END
from agent.nodes import agent_node
from agent.state import AgentState
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

app = graph.compile()

