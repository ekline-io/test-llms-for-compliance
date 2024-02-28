from langchain.chat_models import AzureChatOpenAI

from configurations import AZURE_OPENAI_DEPLOYMENT_NAME


class LLMBuilder:

    @staticmethod
    async def build_llm(llm_type: str):
        """This function takes in the type of LLM and returns the corresponding LLM class."""
        if llm_type == 'azure_openai':
            return AzureChatOpenAI
        else:
            raise ValueError("Invalid LLM type")

    @staticmethod
    async def build_llm_params(llm_type: str):
        """This function takes in the type of LLM and returns the corresponding LLM parameters."""
        if llm_type == 'azure_openai':
            return {
                "deployment_name": AZURE_OPENAI_DEPLOYMENT_NAME,
                "temperature": 0.1,
            }
        else:
            raise ValueError("Invalid LLM type")
