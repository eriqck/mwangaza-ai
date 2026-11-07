
from app.assistant_service import answer_question


def test_question_without_transaction_id():
    result = answer_question("Why did my payment fail?")

    assert result["answered"] is False
    assert "transaction ID" in result["answer"]


def test_question_about_failed_transaction():
    result = answer_question("Why did transaction TXN-1042 fail?")

    assert result["answered"] is True
    assert result["transaction_id"] == "TXN-1042"
    assert "Insufficient funds" in result["answer"]


def test_question_about_successful_transaction():
    result = answer_question("What is the status of TXN-1043?")

    assert result["answered"] is True
    assert result["transaction_id"] == "TXN-1043"
    assert "SUCCESS" in result["answer"]


def test_question_about_transaction_details():
    result = answer_question("Show details for TXN-1042")

    assert result["answered"] is True
    assert "2500.00 KES" in result["answer"]
    assert "FAILED" in result["answer"]
    assert "Insufficient funds" in result["answer"]


def test_question_about_unknown_transaction():
    result = answer_question("Explain TXN-9999")

    assert result["answered"] is False
    assert "could not find" in result["answer"]


def test_unrelated_question():
    result = answer_question("Hello, how are you?")

    assert result["answered"] is False
    assert "payment-related question" in result["answer"]
