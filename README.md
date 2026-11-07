# Mwangaza AI — AI-Powered Payment Operations Assistant

**Mwangaza AI** is an AI-powered payment operations assistant designed around Kenyan payment workflows. It helps users understand transaction outcomes through natural-language conversations backed by verified PostgreSQL transaction records.

**Live Demo:** https://mwangaza-ai.onrender.com  
**GitHub Repository:** https://github.com/eriqck/mwangaza-ai

## Project Overview

Mwangaza AI combines a FastAPI backend, PostgreSQL database and Google's Gemini generative AI to provide clear explanations of payment outcomes.

Users interact with the application through a responsive web-based chat interface. When a question is submitted, the backend identifies the request, retrieves the relevant transaction record and provides verified transaction information to Gemini for explanation.

PostgreSQL remains the authoritative source of financial facts. Gemini generates natural-language explanations but does not independently determine transaction amounts, statuses or failure reasons.

The application also includes a database-generated fallback response when the AI service is unavailable.

This project demonstrates practical application engineering involving generative AI, backend development, database integration, API design, frontend development, cloud deployment, automated testing and responsible AI implementation.

## System Architecture
<img width="2252" height="1440" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/c57f1a38-b51f-4c5f-b158-f4595c5a1e54" />


## Current Features

### AI Payment Assistant
- Natural-language payment questions.
- Gemini-powered transaction explanations.
- Rule-based question classification.
- Transaction ID extraction and validation.
- Database-grounded responses.
- Factual fallback responses when Gemini is unavailable.
- Handling of unknown transaction IDs.

### Transaction Management
- PostgreSQL-backed transaction storage.
- Transaction retrieval by ID.
- Transaction listing.
- Case-insensitive transaction ID matching.
- Transaction outcome explanations.
- Fictional Kenyan shilling (KES) transaction records.

### Web Interface
- Responsive HTML, CSS and JavaScript chat interface.
- Interactive sample questions.
- Real-time communication with the FastAPI backend.
- User and assistant chat messages.
- Loading and error handling.
- Clean, banking-inspired interface.

### Reliability and Testing
- API input validation.
- Appropriate HTTP error responses.
- Automated testing with pytest.
- Gemini integration testing.
- Database fallback testing.
- Manual prompt-injection scenario testing.

## Live Application

Try the public application:

https://mwangaza-ai.onrender.com

Example questions:

- Why did transaction TXN-1042 fail?
- What is the status of TXN-1043?
- What is the status of TXN-9999?

**Demonstration notice:** The application currently uses fictional transaction records. It is not connected to a live bank, payment gateway or customer account.

The application is hosted on Render's free instance, which may take a short time to wake after inactivity.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Database | PostgreSQL |
| Cloud Database | Neon |
| Generative AI | Google Gemini API |
| AI SDK | Google Gen AI SDK |
| Database Driver | Psycopg |
| API Server | Uvicorn |
| Data Validation | Pydantic |
| Environment Management | python-dotenv |
| Automated Testing | pytest |
| Version Control | Git, GitHub |
| Application Hosting | Render |

## System Architecture

The application separates transaction data retrieval from AI-generated explanations.

### Request Workflow

1. A user submits a payment-related question through the web interface.
2. JavaScript sends the question to the FastAPI backend.
3. The question classifier identifies the user's intent.
4. The assistant extracts and validates the transaction ID.
5. The transaction service retrieves the corresponding record from PostgreSQL.
6. The backend supplies the verified transaction information and user question to Gemini.
7. Gemini generates a natural-language explanation using the supplied facts.
8. The backend returns the response to the frontend.
9. The chat interface displays the explanation.

If Gemini is unavailable, the backend returns a factual explanation generated directly from the transaction record.

### Architecture Diagram

```text
             USER
              |
              v
     WEB CHAT INTERFACE
       HTML / CSS / JS
              |
              v
        FASTAPI BACKEND
              |
       QUESTION CLASSIFIER
              |
              v
      ASSISTANT SERVICE
              |
              v
      TRANSACTION SERVICE
              |
              v
       POSTGRESQL (NEON)
       Verified Records
              |
              v
       VERIFIED CONTEXT
              |
              v
         GEMINI API
              |
              v
     NATURAL-LANGUAGE ANSWER
              |
              v
       WEB CHAT INTERFACE
```

## Reliability and Responsible AI

Financial applications require reliable data handling. Mwangaza AI follows several principles:

- **Database authority:** PostgreSQL is the authoritative source of transaction information.
- **Restricted AI context:** Gemini receives only the transaction information required to answer the question.
- **No direct database access:** The language model cannot independently query or modify the database.
- **Grounded explanations:** The model is instructed not to invent transaction amounts, statuses, failure reasons, refunds or reversals.
- **Fallback handling:** If Gemini is unavailable, the application uses a factual database-generated explanation.
- **Unknown transaction handling:** Unknown transaction IDs are rejected rather than passed to Gemini for speculation.
- **Prompt-injection awareness:** User instructions attempting to override the assistant's financial accuracy rules are treated as untrusted input.

Manual prompt-injection testing was performed to verify that the assistant continued reporting the recorded transaction outcome.

These controls demonstrate an approach to integrating generative AI into financial workflows while preserving the authority of structured financial records. They are not a substitute for a full production security audit.

## Deployment Architecture

The application is publicly accessible through Render.

| Service | Platform |
|---|---|
| FastAPI application | Render |
| PostgreSQL database | Neon |
| Generative AI | Google Gemini |
| Source code | GitHub |

The frontend and backend are served from the same FastAPI application. This allows the chat interface to communicate with the backend through the same application origin without requiring a separate frontend deployment.

Production configuration is managed through environment variables.

## Project Structure

```text
mwangaza-ai/
│
├── app/
│   ├── static/
│   │   ├── index.html
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── main.py
│   ├── database.py
│   ├── transaction_service.py
│   ├── assistant_service.py
│   ├── gemini_service.py
│   ├── question_classifier.py
│   └── schemas.py
│
├── database/
│   ├── schema.sql
│   └── seed.sql
│
├── tests/
│   ├── test_main.py
│   ├── test_transaction_service.py
│   ├── test_assistant_service.py
│   └── test_question_classifier.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serves the Mwangaza AI web interface |
| GET | `/health` | Checks application health |
| GET | `/transactions` | Lists transaction records |
| GET | `/transactions/{transaction_id}` | Retrieves a transaction |
| GET | `/transactions/{transaction_id}/explanation` | Explains a transaction outcome |
| POST | `/assistant/ask` | Submits a question to the payment assistant |

Interactive API documentation is available at:

`https://mwangaza-ai.onrender.com/docs`

### Example Assistant Request

```json
{
  "question": "Why did transaction TXN-1042 fail?"
}
```

### Example Transaction Record

```json
{
  "transaction_id": "TXN-1042",
  "amount": 2500.0,
  "currency": "KES",
  "status": "FAILED",
  "reason": "Insufficient funds"
}
```

The assistant retrieves these verified facts and uses Gemini to generate a natural-language explanation.

## Running Locally

### Prerequisites

Install:

- Python 3.10 or later
- PostgreSQL
- Git
- A Google AI Studio API key

### 1. Clone the repository

```bash
git clone https://github.com/eriqck/mwangaza-ai.git
cd mwangaza-ai
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Create the PostgreSQL database

Connect to PostgreSQL:

```bash
psql -U postgres -h localhost -p 5432
```

Create the database:

```sql
CREATE DATABASE mwangaza_ai;
```

Exit:

```sql
\q
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/mwangaza_ai

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=YOUR_CONFIGURED_GEMINI_MODEL
```

Replace the placeholders with your actual configuration.

Obtain a Gemini API key through Google AI Studio:

https://aistudio.google.com/

Never commit `.env`, expose API keys or publish database credentials.

### 6. Create the database schema

```bash
psql -U postgres -h localhost -p 5432 -d mwangaza_ai -f database/schema.sql
```

### 7. Seed sample transaction records

```bash
psql -U postgres -h localhost -p 5432 -d mwangaza_ai -f database/seed.sql
```

The seed script uses conflict handling to avoid duplicate transaction IDs.

### 8. Start the application

```bash
python -m uvicorn app.main:app --reload
```

### 9. Access the application

- Web interface: http://127.0.0.1:8000/
- API health: http://127.0.0.1:8000/health
- Transactions: http://127.0.0.1:8000/transactions
- API documentation: http://127.0.0.1:8000/docs

## Automated Testing

Run the test suite:

```bash
python -m pytest -v
```

The test suite currently contains **25 passing tests** covering:

- API endpoints.
- Transaction retrieval.
- Question classification.
- Assistant responses.
- Transaction ID validation.
- Gemini response simulation through mocking.
- Database fallback when Gemini is unavailable.

Gemini responses are mocked during automated testing to avoid unnecessary external API requests.

## Future Improvements

Potential future development includes:

- Integration with payment providers and banking APIs.
- Real-time payment status notifications.
- Transaction reconciliation workflows.
- Role-based access control for payment operations teams.
- Audit logging and monitoring.
- More advanced natural-language question handling.
- Secure authentication and authorization.
- Production-grade deployment, observability and security controls.

These are planned improvements, not currently implemented features.

## Author

**Eric Mwangi**  
Software Engineer | Software & AI Application Development

GitHub: https://github.com/eriqck

LinkedIn: https://linkedin.com/in/developererick

Portfolio: https://developererik.me

---

*Mwangaza AI is a demonstration project exploring how generative AI can support payment operations while keeping financial facts grounded in structured database records.*
