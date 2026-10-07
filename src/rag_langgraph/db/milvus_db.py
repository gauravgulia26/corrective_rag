from langchain_huggingface import HuggingFaceEmbeddings
from langchain_milvus import Milvus
from langchain_milvus.function import BM25BuiltInFunction


def get_vector_store(
    embedding_model: HuggingFaceEmbeddings, db_path: str, collection_name: str
) -> Milvus:
    vector_store = Milvus(
        embedding_function=embedding_model,
        connection_args={"uri": db_path},
        collection_name=collection_name,
        builtin_function=BM25BuiltInFunction(),
        vector_field=["dense", "sparse"],
        auto_id=True,
        index_params=[
            {
                "index_type": "AUTOINDEX",
                "metric_type": "COSINE",
            },
            {
                "index_type": "SPARSE_INVERTED_INDEX",
                "metric_type": "BM25",
            },
        ],
    )
    return vector_store
