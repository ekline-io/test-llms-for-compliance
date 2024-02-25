from app.llm.builder import LLMBuilder


async def llm(llm_type, conversation, **kwargs):
    """This function takes in a conversation and returns the response from the LLM."""
    # The LLM is an instance of the AzureChatOpenAI class
    llm = await AzureChatOpenAI()
    # Initiate the LLM with kwargs
    await llm.init(**kwargs)
    # Get the response from the LLM
    response = await llm(conversation)
    return response.output
