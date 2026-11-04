from pydantic import BaseModel, Field


class AssistantRequest(BaseModel):
    question: str = Field(
        min_length=1,
        description="The user's payment-related question",
    )


class AssistantResponse(BaseModel):
    answered: bool
    transaction_id: str | None = None
    answer: str
    source: str | None = None