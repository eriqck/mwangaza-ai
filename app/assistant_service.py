
import re

from app.transaction_service import explain_transaction


def answer_question(question: str) -> dict:
    """Answer transaction questions using recorded transaction data."""

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

    return {
        "answered": True,
        "transaction_id": transaction_id,
        "answer": result["explanation"],
        "source": "transaction_record",
    }
