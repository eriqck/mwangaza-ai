
from fastapi import FastAPI, HTTPException

from app.transaction_data import TRANSACTIONS
from app.transaction_service import explain_transaction


app = FastAPI(
    title="Mwangaza AI",
    description="AI-powered payment operations assistant",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "Mwangaza AI",
        "message": "Payment operations API is running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/transactions")
def list_transactions():
    return list(TRANSACTIONS.values())


@app.get("/transactions/{transaction_id}/explanation")
def get_transaction_explanation(transaction_id: str):
    result = explain_transaction(transaction_id)

    if not result["found"]:
        raise HTTPException(
            status_code=404,
            detail=result["explanation"],
        )

    return result


@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    transaction = TRANSACTIONS.get(transaction_id.upper())

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found",
        )

    return transaction
