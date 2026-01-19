from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import crud, schemas, dependencies, models

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

@router.get("/", response_model=List[schemas.EventResponse])
def read_events(status: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    events = crud.get_events(db, status=status, skip=skip, limit=limit)
    return events

@router.get("/{event_id}", response_model=schemas.EventResponse)
def read_event(event_id: int, db: Session = Depends(dependencies.get_db)):
    db_event = crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.post("/{event_id}/join", response_model=schemas.RegistrationResponse)
def join_event(event_id: int, current_user: models.User = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    event = crud.get_event(db, event_id=event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    registration = crud.register_user_for_event(db, user_id=current_user.id, event_id=event_id)
    return registration

# Admin endpoints
@router.post("/", response_model=schemas.EventResponse)
def create_event(event: schemas.EventCreate, current_user: models.User = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    # Simple role check
    if current_user.role != "admin":
         raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_event(db=db, event=event)

@router.delete("/{event_id}", response_model=schemas.EventResponse)
def delete_event(event_id: int, current_user: models.User = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    if current_user.role != "admin":
         raise HTTPException(status_code=403, detail="Not authorized")
    db_event = crud.delete_event(db, event_id=event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
