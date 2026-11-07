Mwangaza AI
An AI-powered payment operations assistant built around Kenyan payment workflows.

Mwangaza AI helps users understand payment outcomes by combining PostgreSQL-backed transaction retrieval with Google's Gemini generative AI.

The application retrieves verified transaction records from PostgreSQL and uses Gemini to generate clear, natural-language explanations. Financial facts remain grounded in database records, while fallback handling ensures the assistant can still provide factual responses when the AI service is unavailable.

This project demonstrates backend application development, generative AI integration, database engineering, API design, automated testing, and responsible AI application development.
Current Features
- REST API built with FastAPI.
- PostgreSQL database for persistent transaction storage.
- Gemini API integration for natural-language explanations.
- Database-grounded AI responses.
- Health-check endpoint.
- Endpoint for listing transactions.
- Transaction lookup by ID, with case-insensitive matching.
- Transaction explanations based on recorded payment outcomes.
- Payment assistant endpoint for transaction-related questions.
- Rule-based question classification.
- Automatic database fallback when Gemini is unavailable.
- Input validation and appropriate HTTP 404 responses.
- Automated tests using pytest.
- Fictional Kenyan shilling (KES) transaction records.
Technology Stack
- Python
- FastAPI
- PostgreSQL
- Psycopg
- Google Gemini API
- Google Gen AI SDK
- Uvicorn
- Pydantic
- python-dotenv
- pytest
- Git
Project Structure
mwangaza-ai/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── transaction_service.py
│   ├── assistant_service.py
│   ├── gemini_service.py
│   ├── question_classifier.py
│   └── schemas.py
├── database/
│   ├── schema.sql
│   └── seed.sql
├── tests/
│   ├── test_main.py
│   ├── test_transaction_service.py
│   ├── test_assistant_service.py
│   └── test_question_classifier.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

Architecture
Mwangaza AI separates financial data retrieval from AI-generated explanations.

The application follows this workflow:
1. A user submits a payment-related question.
2. The question classifier identifies the user's intent.
3. The assistant extracts the transaction ID.
4. The transaction service retrieves the corresponding record from PostgreSQL.
5. The backend validates that the transaction exists.
6. Gemini receives the user's question and the verified transaction facts.
7. Gemini generates a natural-language explanation.
8. The API returns the answer to the user.
Reliability and AI Safety
The system follows several important principles:
- PostgreSQL is the authoritative source of transaction information.
- Gemini does not have direct database access.
- The model receives only the transaction information required to answer the question.
- The model is instructed not to invent transaction amounts, statuses, or failure reasons.
- If Gemini is unavailable, the assistant falls back to a factual database-generated explanation.
- Unknown transaction IDs are rejected rather than passed to Gemini for speculation.
This approach demonstrates how generative AI can be integrated into financial applications while maintaining control over the underlying financial facts.
Run Locally
1. Prerequisites
Install:
- Python 3.10 or later
- PostgreSQL
- Git
- A Google AI Studio API key
2. Clone the repository
git clone https://github.com/eriqck/mwangaza-ai.git
cd mwangaza-ai

3. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

4. Install dependencies
python -m pip install -r requirements.txt

5. Create the PostgreSQL database
Connect to PostgreSQL:
psql -U postgres -h localhost -p 5432

Create the database:
CREATE DATABASE mwangaza_ai;
\q

6. Configure environment variables
Create a .env file in the project root:
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/mwangaza_ai

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=YOUR_CONFIGURED_GEMINI_MODEL

Replace the placeholders with your actual configuration.

Obtain your Gemini API key through Google AI Studio.

Never commit .env, expose API keys, or publish database credentials.
7. Create the database table and sample records
Run:
psql -U postgres -h localhost -p 5432 -d mwangaza_ai -f database/schema.sql

Then:
psql -U postgres -h localhost -p 5432 -d mwangaza_ai -f database/seed.sql

The seed script uses conflict handling to avoid duplicate transaction IDs.
8. Start the API
python -m uvicorn app.main:app --reload

9. Explore the API
- Health check: http://127.0.0.1:8000/health
- List transactions: http://127.0.0.1:8000/transactions
- Interactive API documentation: http://127.0.0.1:8000/docs
API Endpoints
Method	Endpoint	Description
GET	/	API welcome message
GET	/health	Check API health
GET	/transactions	List transactions
GET	/transactions/{transaction_id}	Retrieve a transaction
GET	/transactions/{transaction_id}/explanation	Explain a transaction outcome
POST	/assistant/ask	Ask a payment-related question


Example Assistant Request
{
  "question": "Why did transaction TXN-1042 fail?"
}

The assistant retrieves the corresponding transaction record and uses Gemini to explain the recorded outcome.

Example transaction data:
{
  "transaction_id": "TXN-1042",
  "amount": 2500.0,
  "currency": "KES",
  "status": "FAILED",
  "reason": "Insufficient funds"
}

The assistant uses these verified facts to formulate its response.
Run Tests
python -m pytest -v

The automated tests cover:
- API endpoints.
- Transaction retrieval.
- Question classification.
- Assistant responses.
- Gemini response simulation through mocking.
- Database fallback when Gemini is unavailable.
The assistant tests use mocked Gemini responses to avoid unnecessary external API calls during automated testing.