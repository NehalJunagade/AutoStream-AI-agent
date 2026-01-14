from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    messages: List[str]
    lead: Dict
