def classify_question(question: str)-> str:
    """Identify what the user wants to know about a transaction"""

    normalized_question = question.lower().strip()

    failure_keywords = [
    "why did",
    "why was",
    "fail",
    "failed",
    "failure",
    "unsuccessful",
    "declined",
]

    status_keywords = [
        "status",
        "successful",
        "success",
        "completed",
        "pending"
    ]

    details_keyword = [
        "details",
        "show",
        "information",
        "amount",
        "transaction details",
        "explain",
    ]

    if any(word in normalized_question for word in failure_keywords):
        return "failure_explanation"

    if any(word in normalized_question for word in status_keywords):
        return "status_check"

    if any(word in normalized_question for word in details_keyword):
        return "transaction_details"

    return "unknown"
    