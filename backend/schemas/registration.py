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

# New schema for volunteer details in registration
class VolunteerDetails(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    registration_date: datetime
    status: str
    
    class Config:
        from_attributes = True

# New schema for event with registrations
class EventWithRegistrations(BaseModel):
    id: int
    title: str
    description: str
    location: str
    event_date: str
    start_time: str
    end_time: str
    status: str
    volunteer_count: int
    volunteers: list[VolunteerDetails]
    
    class Config:
        from_attributes = True

