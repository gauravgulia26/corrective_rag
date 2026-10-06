from langgraph.graph.state import CompiledStateGraph
from rich.console import Console
from rich.syntax import Syntax

console = Console()


def print_mermaid(graph: CompiledStateGraph) -> None:
    """
    Print the compiled LangGraph workflow as Mermaid syntax
    with Rich terminal formatting.
    """
    mermaid = graph.get_graph().draw_mermaid()

    console.print(
        Syntax(
            mermaid,
            "text",
            theme="monokai",
            line_numbers=False,
        )
    )
