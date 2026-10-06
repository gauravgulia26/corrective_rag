from rich import print

from rag_langgraph.graph import workflow


def main():
    intitial_state = {
        "user_query": "How this Policy is going to help postgrduate students and phd students. What are the entry and exit options for a student in this."
    }
    response = workflow.invoke(intitial_state)
    print(response)


if __name__ == "__main__":
    main()
