from fastapi import FastAPI
import uvicorn

from configurations import auth_host, auth_port, auth_reload
from data_models import CheckComplianceRequest, CheckComplianceResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"service": "churn-prediction", "version": "0.0.1"}


@app.post("/check_compliance")
async def check_compliance(request: CheckComplianceRequest):

    return CheckComplianceResponse(status="success", compliant=True, findings={})


if __name__ == "__main__":
    uvicorn.run("main:app", host=auth_host, port=auth_port, reload=auth_reload)
