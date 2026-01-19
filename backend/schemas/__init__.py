from .user import UserBase, UserCreate, UserLogin, UserResponse, UserWithEvents
from .event import EventBase, EventCreate, EventResponse
from .registration import RegistrationBase, RegistrationCreate, RegistrationResponse
from .contact import ContactMessageCreate, ContactMessageResponse
from .token import Token, TokenData

# Fix forward references for Pydantic v2 (model_rebuild is preferred but update_forward_refs for compatibility if using v1)
try:
    UserWithEvents.model_rebuild()
except AttributeError:
    UserWithEvents.update_forward_refs(RegistrationResponse=RegistrationResponse)
