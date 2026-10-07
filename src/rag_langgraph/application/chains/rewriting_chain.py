from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from rag_langgraph.config import GroqConfig
from rag_langgraph.models import get_chat_model
from rag_langgraph.utils.loaders import load_prompt

__cfg = GroqConfig(model_name="openai/gpt-oss-20b", temperature=0.2)
__llm = get_chat_model(llm_config=__cfg)
prompt = load_prompt(
    path="/home/gaurav/Documents/rag_langgraph/src/rag_langgraph/prompts/rewriting_prompt.md"
)


def get_rewriting_chain() -> Runnable:
    prompt_template = ChatPromptTemplate(
        [("system", prompt), ("human", "{user_query}")]
    )
    return prompt_template | __llm
