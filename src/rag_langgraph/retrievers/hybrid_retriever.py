import os
from functools import lru_cache

from dotenv import load_dotenv
from langchain_milvus import Milvus

from rag_langgraph.config.paths import DATABASE_DIR
from rag_langgraph.db import get_milvus_store
from rag_langgraph.models.embeddings_models import get_embedding_model

load_dotenv()


@lru_cache
def get_hybrid_retriever(collection_name: str, database_name: str) -> Milvus:
    key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    embedding_model = get_embedding_model(api_key=key)
    return get_milvus_store(
        embedding_model=embedding_model,
        db_path=str(DATABASE_DIR / database_name),
        collection_name=collection_name,
    )
