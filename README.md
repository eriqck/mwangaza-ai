# Mwangaza AI

An AI-assisted payment operations application built around Kenyan payment workflows. Mwangaza AI helps users understand transaction outcomes through a REST API backed by PostgreSQL, with explanations grounded in verified transaction records.

This project demonstrates backend application development, database integration, API design, testing, and reliable handling of payment information.

## Current Features

- REST API built with FastAPI.
- PostgreSQL database for persistent transaction storage.
- Health-check endpoint.
- Endpoint for listing transactions.
- Transaction lookup by ID, with case-insensitive matching.
- Transaction explanations based on recorded payment outcomes.
- Payment assistant endpoint for transaction-related questions.
- Input validation and appropriate HTTP 404 responses.
- Automated tests using pytest.
- Fictional Kenyan shilling (KES) transaction records.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- Psycopg
- Uvicorn
- Pydantic
- pytest
- Git

## Project Structure

```text
mwangaza-ai/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── transaction_service.py
│   ├── assistant_service.py
│   ├── question_classifier.py
│   └── schemas.py
├── database/
│   ├── schema.sql
│   └── seed.sql
├── tests/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Run Locally

### 1. Prerequisites

Install:
- Python 3.10 or later
- PostgreSQL
- Git

### 2. Clone the repository

```powershell
git clone https://github.com/eriqck/mwangaza-ai.git
cd mwangaza-ai
```

### 3. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Create the PostgreSQL database

Connect to PostgreSQL:

```powershell
psql -U postgres -h localhost -p 5432
```

Create the database:

```sql
CREATE DATABASE mwangaza_ai;
\q
```

### 6. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/mwangaza_ai
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

Never commit `.env` or expose database credentials.

### 7. Create the database table and sample records

Run:

```powershell
psql -U postgres -h localhost -p 5432 -d mwangaza_ai -f database/schema.sql
```

Then:

```powershell
psql -U postgres -h localhost -p 5432 -d mwangaza_ai -f database/seed.sql
```

The seed script uses conflict handling to avoid duplicate transaction IDs.

### 8. Start the API

```powershell
python -m uvicorn app.main:app --reload
```

### 9. Explore the API

- Health check: http://127.0.0.1:8000/health
- List transactions: http://127.0.0.1:8000/transactions
- Interactive API documentation: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| GET | `/transactions` | List transactions |
| GET | `/transactions/{transaction_id}` | Retrieve a transaction |
| GET | `/transactions/{transaction_id}/explanation` | Explain a transaction outcome |
| POST | `/assistant/ask` | Ask a payment-related question |

Example assistant request:

```json
{
  "question": "Why did transaction TXN-1042 fail?"
}
```

The assistant retrieves the corresponding transaction record and returns an explanation based on the stored information.

## Run Tests

```powershell
python -m pytest -v
```

The tests cover API endpoints, transaction retrieval, question classification, and assistant responses.

## Architecture and Reliability

Mwangaza AI separates transaction retrieval from question interpretation.

- PostgreSQL stores the authoritative transaction records.
- The transaction service retrieves verified information.
- The question classifier identifies the user's intent.
- The assistant service constructs responses using retrieved records.

The current assistant uses a rule-based question classifier and database-backed retrieval. It does not yet use a generative language model.

This separation helps prevent unsupported financial claims: transaction facts come from stored records rather than being invented by an AI model.

## Roadmap

- [x] Build the initial payment operations API.
- [x] Add automated tests.
- [x] Integrate PostgreSQL.
- [x] Implement transaction explanations.
- [x] Build a database-backed payment assistant.
- [x] Add repeatable database schema and seed scripts.
- [ ] Improve natural-language understanding.
- [ ] Explore controlled AI-assisted responses.
- [ ] Add audit logging and stronger error handling.
- [ ] Build a user-facing interface.
- [ ] Evaluate response accuracy and safe fallback behavior.

## Data and Security

All transaction records are fictional and intended for development and testing.

No real customer information, bank credentials, or live payment integrations are used.

Mwangaza AI is a learning and portfolio prototype, not a production banking or payment system.