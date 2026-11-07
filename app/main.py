from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.transaction_service import (
    explain_transaction,
    get_transaction_records,
    get_transaction_record,
)
from app.assistant_service import answer_question
from app.schemas import AssistantRequest, AssistantResponse


app = FastAPI(
    title="Mwangaza AI",
    description="AI-powered payment operations assistant",
    version="0.1.0",
)

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


@app.get("/")
def root():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/transactions")
def list_transactions():
    return get_transaction_records()


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
    transaction = get_transaction_record(transaction_id)

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found",
        )

    return transaction


@app.post(
    "/assistant/ask",
    response_model=AssistantResponse,
)
def ask_assistant(payload: AssistantRequest):
    return answer_question(payload.question)
