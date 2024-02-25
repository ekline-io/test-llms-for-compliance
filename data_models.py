from pydantic import BaseModel


class CheckComplianceRequest(BaseModel):
    web_page_url: str
    compliance_policy: str


class CheckComplianceResponse(BaseModel):
    status: str
    compliant: bool
    findings: dict
