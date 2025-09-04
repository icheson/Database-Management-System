# Clinic-FastAPI-CRUD

Simple CRUD API for Patients & Appointments using FastAPI + MySQL + SQLAlchemy.

## Prerequisites
- Python 3.8+
- MySQL Server running
- Database `clinic_booking_system` already created (run Question-1 SQL file if you haven't)

## Quick Start
```bash
git clone https://github.com/your-username/clinic-fastapi-crud.git
cd clinic-fastapi-crud
python -m venv venv && source venv/bin/activate   # Win: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # add your MySQL credentials
uvicorn app.main:app --reload
