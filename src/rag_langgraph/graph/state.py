from typing import TypedDict


class AgentState(TypedDict):
    user_query: str
    noul_response: float
    need_rewriting: bool
    rewriting_confidence: float
    refined_query: str
