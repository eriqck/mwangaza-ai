
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Mwangaza AI",
    description="AI-powered payment operations assistant",
    version="0.1.0",
)

#fictional payment records for development and testing

TRANSACTIONS = {
    "TXN-1042": {
        "transaction_id": "TXN-1042",
        "amount": 2500.00,
        "currency": "KES",
        "status": "FAILED",
        "reason": "Insufficient funds",
    },
    "TXN-1043": {
        "transaction_id": "TXN-1043",
        "amount": 1200.00,
        "currency": "KES",
        "status": "SUCCESS",
        "reason": None,
    },
}



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

@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    transaction = TRANSACTIONS.get(transaction_id.upper())

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found",
        )

    return transaction
