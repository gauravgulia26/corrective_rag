from .chains.rewriting_chain import get_rewriting_chain, prompt


class ChainLoader:
    GET_REWRITING_PROMPT = prompt

    @staticmethod
    def get_rewriting_runnable():
        """Input_Variable:user_query"""
        return get_rewriting_chain()
