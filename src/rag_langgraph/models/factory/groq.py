from functools import lru_cache

from langchain_groq import ChatGroq

from rag_langgraph.config.groq_config import GroqConfig
from rag_langgraph.settings.base import LoadBaseSettings


@lru_cache
def get_llm(llm_config: GroqConfig) -> ChatGroq:
    sts = LoadBaseSettings(llm_config=llm_config)
    return ChatGroq(
        model=sts.llm_config.model_name,
        temperature=sts.llm_config.temperature,
        max_retries=sts.llm_config.max_retries,
        max_tokens=sts.llm_config.max_tokens,
        reasoning_effort=sts.llm_config.reasoning_effort,
        api_key=sts.groq_api_key,
    )
