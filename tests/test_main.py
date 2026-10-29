from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_list_transactions():
    response = client.get("/transactions")

    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_existing_transactions():
    response = client.get("/transactions/TXN-1042")

    assert response.status_code == 200
    assert response.json()["status"] == "FAILED"
    assert response.json()["currency"] == "KES"

def test_transaction_lookup_is_case_insensitive():
    response = client.get("transactions/txn-1042")

    assert response.status_code == 200
    assert response.json()["transaction_id"] == "TXN-1042"

def test_missing_transaction_returns_404():
    response = client.get("/transactions/TXN-9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Transaction not found"