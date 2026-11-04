from app.assistant_service import answer_question

def test_question_without_transaction_id():
    result = answer_question("why did my payment fail?")

    assert result["answered"] is False
    assert "transaction ID" in result["answer"]

def test_question_about_failed_transaction():
    result = answer_question("why did transaction TXN-1042 fail?")

    assert result["answered"] is True
    
    assert "Insufficient funds" in result["answer"]

def test_question_about_successful_transaction():
    result = answer_question("Did transaction TXN-1043 pass?")

    assert result["answered"] is True
    assert "successful" in result["answer"]

def  test_question_about_unknown_transaction():
    result = answer_question("Did transaction TXN-9999 happen?")

    assert result["answered"] is False
    assert "could not find" in result["answer"]
    

