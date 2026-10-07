from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from .nodes.factory import (
    retriever_node,
    rewriting__check_node,
    rewriting_check_router_node,
    rewriting_node,
)
from .state import AgentState


class AgentGraphBuilder:
    def __init__(self):
        self.graph = StateGraph(AgentState)

    def __register_nodes(self):
        self.graph.add_node(
            "rewriting_check",
            rewriting__check_node,
        )
        self.graph.add_node(
            "rewriting_node",
            rewriting_node,
        )
        self.graph.add_node(
            "retriever_node",
            retriever_node,
        )

    def __register_edges(self):
        self.graph.add_edge(
            START,
            "rewriting_check",
        )

        self.graph.add_conditional_edges(
            "rewriting_check",
            rewriting_check_router_node,
            {
                "retriever_node": "retriever_node",
                "rewriting_node": "rewriting_node",
            },
        )

        self.graph.add_edge(
            "rewriting_node",
            "retriever_node",
        )

        self.graph.add_edge(
            "retriever_node",
            END,
        )

    def get_graph(self) -> CompiledStateGraph:
        self.__register_nodes()
        self.__register_edges()

        return self.graph.compile()
