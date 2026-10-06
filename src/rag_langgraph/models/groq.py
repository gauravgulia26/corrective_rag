from functools import lru_cache
from pathlib import Path

from langchain_groq import ChatGroq

from rag_langgraph.config.groq_config import GroqConfig
from rag_langgraph.config.paths import MODEL_CONFIG_PATH
from rag_langgraph.utils.loaders import load_settings

_DEFAULT_CONFIG_PATH = MODEL_CONFIG_PATH


@lru_cache
def get_llm(param_file_path: str | Path = _DEFAULT_CONFIG_PATH) -> ChatGroq:
    sts = load_settings(
        model_config=GroqConfig,
        param_key="groq",
        param_file_path=param_file_path,
    )
    return ChatGroq(
        model=sts.llm_config.model_name,
        temperature=sts.llm_config.temperature,
        max_retries=sts.llm_config.max_retries,
        max_tokens=sts.llm_config.max_tokens,
        reasoning_effort=sts.llm_config.reasoning_effort,
        api_key=sts.groq_api_key,
    )
