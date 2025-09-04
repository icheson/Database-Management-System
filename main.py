from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

# create tables automatically (dev only)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clinic Booking CRUD API", version="1.0.0")

# ---------------------------------------------------------
# PATIENT ENDPOINTS
# ---------------------------------------------------------
@app.post("/patients", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db=db, patient=patient)

@app.get("/patients", response_model=List[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_patients(db, skip=skip, limit=limit)

@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.put("/patients/{patient_id}", response_model=schemas.Patient)
def update_patient(patient_id: int, payload: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.update_patient(db, patient_id=patient_id, updates=payload)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.delete("/patients/{patient_id}", response_model=schemas.Patient)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.delete_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

# ---------------------------------------------------------
# APPOINTMENT ENDPOINTS
# ---------------------------------------------------------
@app.post("/appointments", response_model=schemas.Appointment)
def create_appointment(appt: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db=db, appt=appt)

@app.get("/appointments", response_model=List[schemas.Appointment])
def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_appointments(db, skip=skip, limit=limit)

@app.get("/appointments/{appointment_id}", response_model=schemas.Appointment)
def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appt = crud.get_appointment(db, appointment_id=appointment_id)
    if db_appt is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appt

@app.put("/appointments/{appointment_id}", response_model=schemas.Appointment)
def update_appointment(appointment_id: int, payload: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    db_appt = crud.update_appointment(db, appointment_id=appointment_id, updates=payload)
    if db_appt is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appt

@app.delete("/appointments/{appointment_id}", response_model=schemas.Appointment)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appt = crud.delete_appointment(db, appointment_id=appointment_id)
    if db_appt is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appt
