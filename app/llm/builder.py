from langchain.chat_models import AzureChatOpenAI


class LLMBuilder:

    @staticmethod
    async def build_llm(llm_type: str):
        """This function takes in the type of LLM and returns the corresponding LLM class."""
        if llm_type == 'azure_openai':
            return AzureChatOpenAI
        else:
            raise ValueError("Invalid LLM type")
