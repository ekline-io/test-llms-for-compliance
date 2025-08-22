# llms-for-compliace

## Description
This service checks webpage copy against the compliance policy and reports the findings.
The service uses the AZURE OPENAI API, which leverages a large language model to generate the compliance report.

## Steps to run the service
1. Clone the repository.
2. Set the configurations in `configurations.py`, updating the Azure key and deployment URL.

#### Docker run
3. Build the docker image with the following command:
```docker build -t llms-for-compliance .```
4. Run the docker container:
```docker run -p 80:80 llms-for-compliance```
5. The service runs on http://localhost:80

#### Local run
3. Install the dependencies:
```pip install -r requirements.txt```
4. Start the service:
```python main.py```
5. The service runs on http://localhost:80

### API Endpoints
1. POST /compliance-check
    - Request Body: 
    ```
    {
        "web_page_url": "The webpage url is here",
        "compliance_policy_url": "The compliance policy is here"
    }
    ```
    - Response:
    ```
    {
        "status": "The status of the API is here",
        "compliant": "The compliance status is here",
        "findings": "The findings (non-compliant results) are here"
    }
    ```

### Architecture
The architecture has three main modules:
1. Configurations: This module manages the configurations for the service. Set the configurations for the service in the `configurations.py` file.
2. Extract: This module extracts the content from any provided webpage URL. It uses Goose to extract webpage content. The builder design pattern in the LLM module allows for including various types of media in this module.
3. LLM: This module checks the compliance of the webpage content against the compliance policy. It also includes a builder to plug in and use any LLM for the compliance check. Currently, the service uses the Azure OpenAI API for compliance checking.

### Results
1. Compliance Check for https://www.joinguava.com/ against the compliance policy https://www.joinguava.com/compliance-policy
    - Request:
    ```
    {
        "web_page_url": "https://www.joinguava.com/",
        "compliance_policy_url": "https://docs.stripe.com/treasury/marketing-treasury"
    }
    ```
    - Response:
    ```
    {
        "status": "success",
        "compliant": false,
        "findings": {
            "Banking Terminology": "The content uses terms like 'business checking account', 'banking', and 'bank accounts' which are prohibited for use by entities that are not state- or federally-chartered banks or credit unions.",
            "Yield Disclosure": "The content does not disclose that the yield percentage is subject to change and the conditions under which it might change. It also does not notify customers whenever the yield percentage has changed.",
            "FDIC Insurance": "The content does not mention FDIC insurance eligibility, the conditions for FDIC pass-through deposit insurance, or the fact that neither the platform nor Stripe are FDIC insured institutions."
        }
    }
    ```
    - Screenshot:
![](resources/sample_results/joinguava_compliance_check.png)


2. Compliance Check for https://www.stripe.com/ against the compliance policy https://www.joinguava.com/compliance-policy
    - Request:
    ```
    {
        "web_page_url": "https://www.stripe.com/",
        "compliance_policy_url": "https://docs.stripe.com/treasury/marketing-treasury"
    }
    ```
    - Response:
    ```
    {
        "status": "success",
        "compliant": true,
        "findings": {}
    }
    ```
    - Screenshot:
   
   ![](resources/sample_results/stripe_compliance_check.png)

### Future Scope
1. Include more LLMs for the compliance check.
2. Include more extractors for webpage content.
3. Try additional techniques to check the compliance of webpage content. 
   1. For example, call the LLM multiple times to extract key information from the compliance policy and use that to validate the webpage content. The prompt implementation of this approach is already in the prompts file, but the results are currently inconsistent, so the simpler approach is used. Further prompt engineering may yield better results.
4. Fine-tune the LLMs to provide more controlled and accurate results.