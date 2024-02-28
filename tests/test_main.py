import pytest

from main import check_compliance
from data_models import CheckComplianceRequest

pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_check_compliance():
    request = CheckComplianceRequest(web_page_url="https://www.guavabank.com",
                                     compliance_policy_url= "https://stripe.com/docs/treasury/marketing-treasury")

    response = await check_compliance(request)
    assert response.status == "success"
    assert response.compliant is False
    assert response.findings is not None
