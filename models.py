from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class Gender(str, enum.Enum):
    M = "M"
    F = "F"
    O = "O"

class Patient(Base):
    __tablename__ = "patients"
    patient_id   = Column(Integer, primary_key=True, index=True)
    first_name   = Column(String(50), nullable=False)
    last_name    = Column(String(50), nullable=False)
    date_of_birth= Column(Date, nullable=False)
    gender       = Column(Enum(Gender), nullable=False)
    phone        = Column(String(25), unique=True, nullable=False)
    email        = Column(String(100), unique=True, nullable=True)
    street       = Column(String(100))
    city         = Column(String(50))
    state        = Column(String(50))
    postal_code  = Column(String(15))
    created_at   = Column(DateTime, server_default="CURRENT_TIMESTAMP")

    appointments = relationship("Appointment", back_populates="patient")

class Appointment(Base):
    __tablename__ = "appointments"
    appointment_id   = Column(Integer, primary_key=True, index=True)
    patient_id       = Column(Integer, ForeignKey("patients.patient_id"))
    doctor_id        = Column(Integer, ForeignKey("doctors.doctor_id"))
    room_id          = Column(Integer, ForeignKey("rooms.room_id"), nullable=True)
    appt_date_time   = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, default=30)
    status           = Column(Enum("Scheduled","Completed","Cancelled","No-Show"), default="Scheduled")
    notes            = Column(Text)

    patient = relationship("Patient", back_populates="appointments")
    doctor  = relationship("Doctor", back_populates="appointments")
