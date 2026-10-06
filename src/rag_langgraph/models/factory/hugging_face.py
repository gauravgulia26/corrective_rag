from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model(
    api_key: str,
    model_name: str = "intfloat/multilingual-e5-base",
    device_type: str = "cuda",
    norm: bool = True,
):
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={
            "device": device_type,
            "token": api_key,
        },
        encode_kwargs={
            "normalize_embeddings": norm,
        },
    )

    return embeddings
