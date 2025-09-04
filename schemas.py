from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, List

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone: str
    email: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int
    created_at: datetime
    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    room_id: Optional[int] = None
    appt_date_time: datetime
    duration_minutes: int = 30
    status: str = "Scheduled"
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    appointment_id: int
    class Config:
        from_attributes = True
