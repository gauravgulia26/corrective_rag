from rag_langgraph.agent.factory import ChainLoader

from ..state import AgentState


def rewriting_node(state: AgentState):
    original_query = state["user_query"]
    chain = ChainLoader.get_rewriting_runnable()
    updated_query = chain.invoke({"user_query": original_query})
    return {"refined_query": updated_query.content}
