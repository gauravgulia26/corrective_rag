from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from .nodes import AgentNode, AgentState


class AgentGraphBuilder:
    GRAPH = StateGraph(state_schema=AgentState)

    @staticmethod
    def get_graph() -> CompiledStateGraph:
        AgentGraphBuilder.GRAPH.add_node("noul_response", AgentNode.noul_response)

        AgentGraphBuilder.GRAPH.add_edge(START, "noul_response")
        AgentGraphBuilder.GRAPH.add_edge("noul_response", END)

        return AgentGraphBuilder.GRAPH.compile()
