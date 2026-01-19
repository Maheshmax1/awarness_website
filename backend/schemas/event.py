from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    description: str
    location: str
    event_date: str
    start_time: str
    end_time: str
    image_url: str
    status: str = "upcoming"

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
