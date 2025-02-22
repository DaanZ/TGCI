from core.chatgpt import llm_strict, llm_chat
from core.history import History


class LLM:

    def __init__(self):
        pass

    def strict(self, history: History, base_model: type):
        pass

    def chat(self, history: History):
        pass


class OpenAILLM(LLM):

    def __init__(self):
        super().__init__()

    def strict(self, history: History, base_model: type):
        return llm_strict(history, base_model=base_model)

    def chat(self, history: History):
        return llm_chat(history)