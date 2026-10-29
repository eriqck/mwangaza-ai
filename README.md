
# Mwangaza AI

An AI-powered payment operations assistant designed around Kenyan payment workflows. The project explores how AI can help users understand transaction outcomes using verified data, with an emphasis on reliability, security, and traceability.

## Current Features

- REST API built with FastAPI.
- Health-check endpoint.
- Endpoint for listing payment transactions.
- Transaction lookup by ID, with case-insensitive matching.
- Clear 404 responses for transactions that do not exist.
- Automated API tests using pytest.
- Fictional KES transaction records for development and testing.

## Technology Stack

- Python
- FastAPI
- Uvicorn
- pytest
- Git

## Run Locally

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install fastapi "uvicorn[standard]" pytest httpx
```

### 3. Start the API

```powershell
python -m uvicorn app.main:app --reload
```

### 4. Explore the API

- Health check: http://127.0.0.1:8000/health
- List transactions: http://127.0.0.1:8000/transactions
- Interactive API documentation: http://127.0.0.1:8000/docs

### 5. Run tests

```powershell
python -m pytest -v
```

## Project Roadmap

- [x] Build the initial payment operations API.
- [x] Add automated tests for core endpoints.
- [ ] Add transaction explanations grounded in verified records.
- [ ] Introduce retrieval and AI-assisted responses.
- [ ] Add validation, error handling, and audit logging.
- [ ] Evaluate answer accuracy and safe fallback behavior.

## Data and Security

The current records are fictional and intended for development only. No real customer or payment data is used. This project is a learning and portfolio prototype, not a production payment system.
