
from app.database import get_connection


def get_transaction_records() -> list:
    """Retrieve all transactions from PostgreSQL."""

    query = """
        SELECT transaction_id, amount, currency, status, reason
        FROM transactions
        ORDER BY id
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

    return [
        {
            "transaction_id": row[0],
            "amount": float(row[1]),
            "currency": row[2],
            "status": row[3],
            "reason": row[4],
        }
        for row in rows
    ]


def get_transaction_record(transaction_id: str):
    """Retrieve one transaction from PostgreSQL."""

    normalized_id = transaction_id.strip().upper()

    query = """
        SELECT transaction_id, amount, currency, status, reason
        FROM transactions
        WHERE transaction_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (normalized_id,))
            row = cursor.fetchone()

    if row is None:
        return None

    return {
        "transaction_id": row[0],
        "amount": float(row[1]),
        "currency": row[2],
        "status": row[3],
        "reason": row[4],
    }


def explain_transaction(transaction_id: str) -> dict:
    """Return a factual explanation using PostgreSQL records."""

    normalized_id = transaction_id.strip().upper()
    transaction = get_transaction_record(normalized_id)

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
        **transaction,
        "explanation": explanation,
        "source": "transaction_record",
    }
