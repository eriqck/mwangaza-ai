from app.question_classifier import  classify_question

def test_classify_failure_question():
    result = classify_question("Why did TXN-1042 fail?")

    assert result == "failure_explanation"


def test_classify_status_question():
    result = classify_question("What is the status of TXN-1043?")

    assert result == "status_check"

def test_classify_details_question():
    result = classify_question("Show details for TXN-1043")

    assert result =="transaction_details"

def test_classify_unknown_question():
    result = classify_question("Hello, how are you?")

    assert result == "unknown"

def test_classification_is_case_insensitive():
    result = classify_question("WHY DID TRANSACTION TXN-1042 FAIL?")
    assert result == "failure_explanation"