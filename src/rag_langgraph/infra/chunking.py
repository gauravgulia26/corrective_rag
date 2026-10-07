import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_experimental.text_splitter import SemanticChunker

from rag_langgraph.config.paths import NEP_PDF_PATH
from rag_langgraph.models.embeddings_models import get_embedding_model

load_dotenv()


def make_chunks():
    key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    embedding_model = get_embedding_model(api_key=key)
    chunks = PyMuPDFLoader(file_path=str(NEP_PDF_PATH)).load_and_split(
        text_splitter=SemanticChunker(
            embeddings=embedding_model,
            breakpoint_threshold_type="percentile",
            breakpoint_threshold_amount=95,
        )
    )
    return chunks
