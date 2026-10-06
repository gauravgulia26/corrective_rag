from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from .nodes.factory import rewriting__check_node, rewriting_node
from .state import AgentState


class AgentGraphBuilder:
    GRAPH = StateGraph(state_schema=AgentState)

    @staticmethod
    def get_graph() -> CompiledStateGraph:
        AgentGraphBuilder.GRAPH.add_node("rewriting_check", rewriting__check_node)
        AgentGraphBuilder.GRAPH.add_node("rewriting_node", rewriting_node)

        AgentGraphBuilder.GRAPH.add_edge(START, "rewriting_check")
        AgentGraphBuilder.GRAPH.add_edge("rewriting_check", "rewriting_node")
        AgentGraphBuilder.GRAPH.add_edge("rewriting_node", END)

        return AgentGraphBuilder.GRAPH.compile()
