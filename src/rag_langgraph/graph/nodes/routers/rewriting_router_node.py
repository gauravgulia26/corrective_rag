from typing import Literal

from ...state import AgentState


def rewriting_check_router_node(
    state: AgentState,
) -> Literal["rewriting_node", "retriever_node"]:
    choice = state["need_rewriting"]
    if choice == "yes":
        return "rewriting_node"
    else:
        return "retriever_node"
