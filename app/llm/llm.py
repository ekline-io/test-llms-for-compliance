import json

from langchain.schema import HumanMessage

from app.llm.builder import LLMBuilder
from app.llm.prompt import get_compliance_metrics_prompt, get_compliance_fidings_prompt


class LLM:

    def __init__(self, llm_type):
        self.llm_type = llm_type
        self.prompt = ""

    async def llm(self) -> str:
        """This function takes in a conversation and returns the response from the LLM."""
        # The LLM is an instance of the AzureChatOpenAI class
        builder = LLMBuilder()
        llm = await builder.build_llm(self.llm_type)
        llm_params = await builder.build_llm_params(self.llm_type)
        # Initiate the LLM with kwargs
        llm = llm(**llm_params)
        # Get the response from the LLM
        response = await llm.agenerate([[self.prompt]])
        return response.generations[0][0].text

    async def run(self, content, policy) -> dict:
        """This function does the following:
        1. Get compliance metrics from the compliance policy
        2. Use compliance metrics and policy to get findings from webpage content
        3. Return the findings
        :param content: The content of the webpage
        :param policy: The compliance policy
        :return: The findings
        """

        # Get the check compliance prompt
        prompt = await get_compliance_fidings_prompt(content, policy)
        self.prompt = HumanMessage(content=prompt)
        # Get the findings from the LLM
        findings = await self.llm()
        findings = json.loads(findings)
        return findings
