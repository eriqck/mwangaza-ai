import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_gemini_client():
    """Create a Gemini client using the configured API key."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    return genai.Client(api_key=api_key)


def generate_response(prompt: str) -> str:
    """Send a prompt to Gemini and return its response."""

    model = os.getenv("GEMINI_MODEL")

    if not model:
        raise RuntimeError("GEMINI_MODEL is not configured.")

    client = get_gemini_client()

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text.strip()