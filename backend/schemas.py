from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# --- Technician Schemas ---
class TechnicianBase(BaseModel):
    name: str
    phone: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class TechnicianCreate(TechnicianBase):
    pass

class TechnicianResponse(TechnicianBase):
    id: int
    status: str

    class Config:
        from_attributes = True


# --- Task Schemas ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    latitude: float
    longitude: float

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    status: str
    created_at: datetime
    technician_id: Optional[int] = None

    class Config:
        from_attributes = True