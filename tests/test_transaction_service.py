from app.transaction_service import explain_transaction

def test_explain_failed_transaction():
    result = explain_transaction("TXN-1042")

    assert result["found"] is True
    assert result["status"] == "FAILED"
    assert result["currency"] == "KES"
    assert "insufficient funds" in result["explanation"].lower()


def test_explain_successful_transaction():
        result = explain_transaction("TXN-1043")


        assert result["found"] is True
        assert result["status"] == "SUCCESS"
        assert result["currency"] == "KES"
        assert "successful" in result["explanation"]

def test_unknown_transaction_returns_not_found():
        result = explain_transaction("TXN-9999")

        assert result["found"] is False
        assert "status" not in result

def test_transaction_id_is_case_insensitive():
        result = explain_transaction("txn-1042")

        assert result["found"] is True
        assert result["transaction_id"] == "TXN-1042"

def test_transaction_id_white_space_is_handled():
        result = explain_transaction(" TXN-1042 ")

        assert result["found"] is True
        assert result["transaction_id"] == "TXN-1042"

def test_failed_transaction_returns_correct_reason():
    result = explain_transaction("TXN-1042")

    assert result["found"] is True
    assert result["reason"] == "Insufficient funds"
