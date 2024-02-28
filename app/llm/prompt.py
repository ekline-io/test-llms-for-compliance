from typing import Optional

from langchain import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


async def get_compliance_metrics_prompt(policy: str) -> str:
    """
    Generate a prompt for the compliance officer to extract key compliance metrics from the policy.
    param policy: str
    :return prompt: str
    """

    PROMPT = """
            You are a compliance officer at a financial institution. 
            You have been provided with a web page with compliance policy. 
            Your task is to evaluate and extract key compliance metrics from the provided policy, 
            such that another officer can use this information to ensure that the institution is 
            compliant with the policy. The metrics should be extracted in a structured format, 
            such as a dictionary or a table. 
            The metrics represent the key areas of compliance that should be monitored in detail.
            The metrics should be relevant to the policy and should be presented in a 
            clear and organized manner. 
            Compliance Policy:{policy}
            """

    response_schema = [
        ResponseSchema(name="compliance_metrics", description="The extracted compliance metrics.")
    ]

    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    format_instructions = output_parser.get_format_instructions()

    prompt_template = PromptTemplate(
        input_variables=["policy"],
        template=PROMPT,
    )
    prompt = prompt_template.format(policy=policy, format_instructions=format_instructions)

    return prompt


async def get_compliance_fidings_prompt(content: str, policy: str) -> str:
    """
    Generate a prompt for the compliance officer to evaluate the content against the policy.
    :param content: str
    :param policy: str
    :return prompt: str
    """
    PROMPT = """
            You are a compliance officer at a financial institution. 
            You have been provided with a website content and a compliance policy.
            Your task is to evaluate the content to determine if it complies with the policy. 
            Provide a structured response that indicates whether the content is compliant with the 
            policy. If the web page is not compliant, 
            provide a list of findings that only detail the areas of non-compliance. 
            Don't show the areas which are compliant.
            The findings should be presented in a clear and organized manner. 
            The output keys should be 'compliant' and 'findings'. 
            The value of key 'compliant' can only be True or False.
            The value of key 'findings' should be a dictionary with the areas of non-compliance and the reasons.
            If the content is compliant, return compliant key as true and findings as empty dictionary.  
            The output should be a valid json, you should validate it.
            There should be no extra characters.
            You should evaluate the content against the policy and not anything else.
            //
            Web Page Content: {content}
            \n\n
            Compliance Policy: {policy}
            """

    prompt_template = PromptTemplate(
        input_variables=["content", "policy"],
        template=PROMPT,
    )
    prompt = prompt_template.format(content=content, policy=policy)
    return prompt

