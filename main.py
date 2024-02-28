from fastapi import FastAPI
import uvicorn

from configurations import auth_host, auth_port, auth_reload, llm_type
from data_models import CheckComplianceRequest, CheckComplianceResponse
from app.extraction.extract_webpage import extract_text_from_url
from app.llm.llm import LLM

app = FastAPI()


@app.get("/")
async def root():
    return {"service": "churn-prediction", "version": "0.0.1"}


@app.post("/check_compliance")
async def check_compliance(request: CheckComplianceRequest):
    content = extract_text_from_url(request.web_page_url)
    policy = extract_text_from_url(request.compliance_policy_url)
    findings = await LLM(llm_type=llm_type).run(content, policy)

    return CheckComplianceResponse(status="success", compliant=findings["compliant"], findings=findings["findings"])


if __name__ == "__main__":
    uvicorn.run("main:app", host=auth_host, port=auth_port, reload=auth_reload)
