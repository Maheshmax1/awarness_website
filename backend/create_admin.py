from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from crud import get_password_hash
import sys

def create_admin():
    print("--- EcoClean Admin Creation Tool ---")
    email = input("Enter Admin Email: ").strip()
    full_name = input("Enter Admin Full Name: ").strip()
    phone = input("Enter Admin Phone Number: ").strip()
    password = input("Enter Admin Password: ").strip()

    if not email or not password:
        print("Error: Email and Password are required.")
        return

    db = SessionLocal()
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            print(f"Error: User with email {email} already exists.")
            return

        # Create Admin
        hashed_pwd = get_password_hash(password)
        admin_user = User(
            email=email,
            full_name=full_name,
            phone=phone,
            hashed_password=hashed_pwd,
            role="admin"
        )
        
        db.add(admin_user)
        db.commit()
        print(f"\nSUCCESS: Admin account created for {email}")
        print("You can now login at /pages/login.html with this account.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()
