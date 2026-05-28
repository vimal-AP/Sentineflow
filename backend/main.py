from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routes import router as api_router

# Auto-generate tables on system boot
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SentinelFlow Engine")

# Configure CORS Middleware so our frontend control dashboard can securely access endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any local frontend application origin to interact
    allow_credentials=True,
    allow_methods=["*"],  # Allows all operations (GET, POST, PUT)
    allow_headers=["*"],
)

# Connect mapped API pathways
app.include_router(api_router, prefix="/api")

@app.get("/")
def home():
    return {"status": "SentinelFlow Engine is running successfully, CORS gates open!"}