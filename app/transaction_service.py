
from app.transaction_data import TRANSACTIONS


def explain_transaction(transaction_id: str) -> dict:
    """Return a factual explanation of a transaction's status."""

    normalized_id = transaction_id.strip().upper()
    transaction = TRANSACTIONS.get(normalized_id)

    if transaction is None:
        return {
            "found": False,
            "transaction_id": normalized_id,
            "explanation": (
                "No transaction was found with this ID. "
                "Check the ID and try again."
            ),
        }

    status = transaction["status"]
    reason = transaction["reason"]

    if status == "FAILED":
        explanation = (
            f"Transaction {normalized_id} failed. "
            f"Recorded reason: {reason}."
        )
    elif status == "SUCCESS":
        explanation = (
            f"Transaction {normalized_id} was successful."
        )
    else:
        explanation = (
            f"Transaction {normalized_id} has status {status}. "
            "Further verification may be needed."
        )

    return {
        "found": True,
        "transaction_id": normalized_id,
        "status": status,
        "amount": transaction["amount"],
        "currency": transaction["currency"],
        "reason": reason,
        "explanation": explanation,
        "source": "transaction_record",
        
    }
