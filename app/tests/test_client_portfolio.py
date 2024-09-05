from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_client_portfolios():
    response = client.get("/api/client-portfolio")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_client_portfolio_by_id():
    response = client.get("/api/client-portfolio/6661c77b343c9f02ad846a9f")
    assert response.status_code == 200
    assert response.json()["id"] == "6661c77b343c9f02ad846a9f"
