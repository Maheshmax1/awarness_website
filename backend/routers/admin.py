from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
import crud, schemas, dependencies, models

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/stats")
def get_dashboard_stats(current_user: models.User = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    if current_user.role != "admin":
         raise HTTPException(status_code=403, detail="Not authorized")
    return crud.get_stats(db)

@router.get("/volunteers", response_model=List[schemas.UserResponse])
def get_volunteers(current_user: models.User = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    if current_user.role != "admin":
         raise HTTPException(status_code=403, detail="Not authorized")
    # For now returning all users, assuming all non-admins are volunteers
    # Real implementation might filter by role="volunteer"
    users = db.query(models.User).filter(models.User.role == "volunteer").all()
    return users

@router.get("/messages", response_model=List[schemas.ContactMessageResponse])
def get_messages(current_user: models.User = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    if current_user.role != "admin":
         raise HTTPException(status_code=403, detail="Not authorized")
    return crud.get_contact_messages(db)
