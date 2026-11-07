import re

from app.question_classifier import classify_question
from app.transaction_service import explain_transaction


def answer_question(question: str) -> dict:
    """Answer payment questions using recorded transaction data."""

    intent = classify_question(question)

    if intent == "unknown":
        return {
            "answered": False,
            "answer": (
                "I can help with payment failures, transaction "
                "statuses, and transaction details. "
                "Please ask a payment-related question."
            ),
            "source": None,
        }

    transaction_ids = re.findall(
        r"\bTXN-\d+\b",
        question.upper(),
    )

    if not transaction_ids:
        return {
            "answered": False,
            "answer": (
                "Please include a transaction ID, "
                "such as TXN-1042, so I can check the record."
            ),
            "source": None,
        }

    transaction_id = transaction_ids[0]
    result = explain_transaction(transaction_id)

    if not result["found"]:
        return {
            "answered": False,
            "answer": (
                f"I could not find transaction {transaction_id}. "
                "Please check the transaction ID."
            ),
            "source": None,
        }

    if intent == "failure_explanation":
        answer = result["explanation"]

    elif intent == "status_check":
        answer = (
            f"Transaction {transaction_id} "
            f"currently has status {result['status']}."
        )

    elif intent == "transaction_details":
        answer = (
            f"Transaction {transaction_id}: "
            f"Amount: {result['amount']:.2f} "
            f"{result['currency']}. "
            f"Status: {result['status']}."
        )

        if result.get("reason"):
            answer += f" Recorded reason: {result['reason']}."

    else:
        answer = "I could not determine how to process your question."

    return {
        "answered": True,
        "transaction_id": transaction_id,
        "answer": answer,
        "source": "transaction_record",
    }