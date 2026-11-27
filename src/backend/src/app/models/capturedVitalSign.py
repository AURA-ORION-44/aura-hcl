"""Define care appointment models, time constraints, and performer associations.

`Appointment` represents a scheduled care action attached to a `Patient` and the
active `Encounter` at planning time. Caregivers are linked in two distinct roles:
`validated_by` (the single `Practitioner` who validated the prescription) and
`performers` (many-to-many via `appointment_performer`, ordered by
`Practitioner.id`). `TimeConstraint` distinguishes single-timestamp care
(`STRONG`, using `scheduled_start` only) from interval care (`WEAK`, spanning
`scheduled_start` to `scheduled_end`).
"""

import datetime
from typing import Any

from app.models import Base
from app.models.encounter import Encounter
from app.models.common import ID

from sqlalchemy import ForeignKey, String, JSON, Numeric, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class Appointment(Base):
  __tablename__ = "captured_vital_sign"

  id: Mapped[int] = mapped_column(ID, primary_key=True, autoincrement=True)
  
  #type of captured vital sign 
  vital_name: Mapped[str] = mapped_column(String(255))
  freq: Mapped[float] = mapped_column(Numeric(10, 2))
  is_unique: Mapped[bool] = mapped_column(Boolean)
  list_values: Mapped[list[list[Any]]] = mapped_column(JSON)
  
  #constraints
  encounter_id: Mapped[int] = mapped_column(ID, ForeignKey("encounter.id"))

