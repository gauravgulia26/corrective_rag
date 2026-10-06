from langchain_typesafe import Choice

from rag_langgraph.models import get_system_one_model

from ..state import AgentState

CLASSIFIER = get_system_one_model()


def noul_response(state: AgentState):
    user_query = state["user_query"]
    response = CLASSIFIER.invoke(
        {
            "state": "We have a user query and this is a RAG System.",
            "questions": {
                "need_rewriting": Choice(
                    instructions=f"Does this query {user_query} needs refinement on its original form for better results from RAG",
                    criteria={
                        "yes": "User query is too short and vague, needs refinement",
                        "no": "User query already contains enough information needed for retrieval",
                    },
                ),
            },
        }
    )

    return {
        "need_rewriting": response.choices["need_rewriting"].choice,
        "rewriting_confidence": response.choices["need_rewriting"].confidence,
    }
