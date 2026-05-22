import requests

BASE_URL = "http://localhost:3000/api"

def test_chatbot_requires_auth():
    response = requests.post(f"{BASE_URL}/openai", json={
        "userMessage": "Hello",
        "conversationId": None
    })
    assert response.status_code == 401