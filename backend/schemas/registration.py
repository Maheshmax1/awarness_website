from pydantic import BaseModel
from datetime import datetime
from .event import EventResponse

class RegistrationBase(BaseModel):
    event_id: int

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationResponse(BaseModel):
    id: int
    event_id: int
    user_id: int
    status: str
    registration_date: datetime
    event: EventResponse # Include event details

    class Config:
        from_attributes = True
