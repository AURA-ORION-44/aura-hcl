import datetime
from typing import Any

from app.models import Base
from app.models.encounter import Encounter
from app.models.common import ID

from sqlalchemy import ForeignKey, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

class Appointment(Base):
  __tablename__ = "vital_signs"

  id: Mapped[int] = mapped_column(ID, primary_key=True, autoincrement=True)
  
  effectiveDate: Mapped[datetime] = mapped_column(DateTime)
  weightKg: Mapped[int] = mapped_column(Integer)
  heightCm: Mapped[int] = mapped_column(Integer)
  
  #constraints
  encounter_id: Mapped[int] = mapped_column(ID, ForeignKey("encounter.id"))
