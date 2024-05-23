import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config.database import engine
from db_models import Base

from routers.auth import get_user_info
from schemas import userPayload
from routers.generative_ai import generative_ai
from routers.segmentation_object_detection import segmentation_object_detection
from routers.airline import airline
from routers.airport import airport
from routers.aircraft import aircraft
from routers.skill import skill
from routers.airbus import airbus
from routers.pilot import pilot


load_dotenv()

app = FastAPI()

# Define CORS settings
origins = ["*"]  # Allow requests from any origin

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/status/health")
def health_check():
    return {'status': 'Healthy'}


@app.get("/status/security-check")
async def root(user: userPayload = Depends(get_user_info)):
    return {"message": f"Hello {user.username} you have the following service: {user.realm_roles}"}


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(generative_ai.router)
app.include_router(segmentation_object_detection.router)
app.include_router(airline.router)
app.include_router(airport.router)
app.include_router(aircraft.router)
app.include_router(airbus.router)
app.include_router(pilot.router)
app.include_router(skill.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host=os.getenv("AIM_APP_HOST", "localhost"), port=int(os.getenv("AIM_APP_PORT", 5000)),
                reload=True)
