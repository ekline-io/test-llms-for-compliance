import pytest

from app.llm.llm import LLM


pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_llm():
    content = """Business Banking for Black America. Create your business checking account for free in minutes with 
    instant access to a virtual debit card. Pay bills, transfer funds, check your balance, and more -- anytime, 
    anywhere from our app. Easily track and manage your cash flow as you grow your business. Easily connect your 
    business checking account to Venmo, Etsy, Shopify, Stripe, and more. Connect your Guava virtual card to Apple 
    Wallet or Google Pay for secure, easy, and quick contactless payments. Export your transaction activity into a 
    CSV file for easy uploading to reconciliation tools. """

    policy = """Marketing Treasury-based servicesMany states have statutory prohibitions on references to "banking,
    " "banks," and "bank accounts" when the entities making these references are not state- or federally-chartered banks 
    or credit unions. """

    llm = LLM(llm_type="azure_openai")
    findings = await llm.run(content, policy)
    assert findings["compliant"] is False
