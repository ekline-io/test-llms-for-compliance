# llms-for-compliace

## Description
This service checks webpage copy against the compliance policy and reports findings.
It is currently powered by the AZURE OPENAI API, which uses the GPT-4 model to generate the compliance report.

## Steps to run the service
1. Clone the repository
2. Set the configurations in configurations.py. Update the Azure key and deployment URL.

#### Docker run
3. Run the following command to build the docker image
```docker build -t llms-for-compliance .```
4. Run the following command to run the docker container
```docker run -p 80:80 llms-for-compliance```
5. The service runs on http://localhost:80

#### Local run
3. Run the following command to install the dependencies
```pip install -r requirements.txt```
4. Run the following command to start the service
```python main.py```
5. The service runs on http://localhost:80

### API Endpoints
1. POST /compliance-check
    - Request Body: 
    ```
    {
        "web_page_url": "The webpage URL is provided here",
        "compliance_policy_url": "The compliance policy URL is provided here"
    }
    ```
    - Response:
    ```
    {
        "status": "The status of the API is provided here",
        "compliant": "The compliance status is provided here",
        "findings": "The findings (non-compliant results) are provided here"
    }
    ```

### Architecture
There are 3 main modules in the architecture:
1. Configurations: This module sets the configurations for the service. Set the configurations for the service in the configurations.py file.
2. Extract: This module extracts any webpage URL given to it. It uses Goose to extract the webpage content. This module uses a builder design to allow for inclusion of any type of media.
3. LLM: This module checks the compliance of the webpage content against the compliance policy. This module includes a builder to support any LLM for compliance checks. Currently, it uses the Azure OpenAI API to check compliance.

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
        "findings":   "findings": {
                                   "Banking Terminology": "The content uses terms like 'business checking account', 'banking', and 'bank accounts' which are prohibited for use by entities that are not state- or federally-chartered banks or credit unions.",
                                   "Yield Disclosure": "The content does not disclose that the yield percentage is subject to change and the conditions under which it might change. It also does not notify customers whenever the yield percentage has changed.",
                                   "FDIC Insurance": "The content does not mention anything about FDIC insurance eligibility, the conditions for FDIC pass-through deposit insurance, or the fact that neither the platform nor Stripe are FDIC insured institutions."
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
1. Include more LLMs for compliance checks.
2. Include more extractors for webpage content.
3. Try other techniques to check the compliance of the webpage content.
   1. Call LLM multiple times to extract key information from the compliance policy and use that to validate the webpage content. The prompt implementation of this is already in the prompts file, but the results are currently less controlled; a simpler approach is used for now. Better results may be achieved with additional prompt engineering work.
4. Fine-tune the LLMs to provide more controlled and better results.