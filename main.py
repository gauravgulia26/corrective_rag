from rag_langgraph.graph.nodes import AgentNode

obj = AgentNode()
response = obj.noul_response(user_query="What is this document about")
print(response)
