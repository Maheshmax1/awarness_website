from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth, events, users, contact, admin

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="EcoClean API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(events.router)
app.include_router(users.router)
app.include_router(contact.router)
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to EcoClean API"}
