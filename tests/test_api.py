import requests
import pytest
from config import OPENAI_API_URL

@pytest.mark.ui
@pytest.mark.api
def test_chatbot_requires_auth():
    response = requests.post(OPENAI_API_URL, json={
        "userMessage": "Hello",
        "conversationId": None
    })
    assert response.status_code == 401