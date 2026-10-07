from rag_langgraph.retrievers.hybrid_retriever import get_hybrid_retriever

from .chunking import make_chunks


def ingest_data():
    collection_name = "NEP_POLICY_PDF"
    database_name = "NEP_POLICY.db"
    db = get_hybrid_retriever(
        collection_name=collection_name, database_name=database_name
    )
    if db.client.has_collection(collection_name):
        stats = db.client.get_collection_stats(collection_name)
        if stats.get("row_count", 0) > 0:
            return f"Collection '{collection_name}' already exists with {stats['row_count']} documents."

    chunks = make_chunks()
    total = len(db.add_documents(documents=chunks))
    return f"{total} Document Inserted into DB"
