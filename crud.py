from sqlalchemy.orm import Session
from . import models, schemas

# ---------- PATIENT ----------
def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: int, updates: schemas.PatientCreate):
    db_patient = get_patient(db, patient_id)
    if not db_patient:
        return None
    for key, val in updates.dict(exclude_unset=True).items():
        setattr(db_patient, key, val)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient(db, patient_id)
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient

# ---------- APPOINTMENT ----------
def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()

def create_appointment(db: Session, appt: schemas.AppointmentCreate):
    db_appt = models.Appointment(**appt.dict())
    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)
    return db_appt

def update_appointment(db: Session, appointment_id: int, updates: schemas.AppointmentCreate):
    db_appt = get_appointment(db, appointment_id)
    if not db_appt:
        return None
    for key, val in updates.dict(exclude_unset=True).items():
        setattr(db_appt, key, val)
    db.commit()
    db.refresh(db_appt)
    return db_appt

def delete_appointment(db: Session, appointment_id: int):
    db_appt = get_appointment(db, appointment_id)
    if db_appt:
        db.delete(db_appt)
        db.commit()
    return db_appt
