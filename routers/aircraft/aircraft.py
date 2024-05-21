import uuid
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import aircraftModelModel
from config.database import SessionLocal
from schemas.aircraftSchema import aircraftSchema
from ..auth import get_user_info
from schemas.userPayload import userPayload


router = APIRouter(
    prefix='/aircraft',
    tags=['Aircraft Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_aircraft', status_code=status.HTTP_200_OK)
async def get_all_aircraft(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(aircraftModelModel).all()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.get('/get_aircraft/{id}', status_code=status.HTTP_200_OK)
async def get_aircraft(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(aircraftModelModel).filter(aircraftModelModel.aircraftModelId == id).first()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/add_aircraft", status_code=status.HTTP_201_CREATED)
async def add_aircraft(db: db_dependency, aircraft_data: aircraftSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        aircraft_model_model = aircraftModelModel(
            aircraftModelId=uuid.uuid4(),
            modelName=aircraft_data.modelName,
        )

        db.add(aircraft_model_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.put("/update_aircraft/{id}", status_code=status.HTTP_201_CREATED)
async def update_aircraft(db: db_dependency, aircraft_data: aircraftSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        aircraft_model_model = db.query(aircraftModelModel).filter(aircraftModelModel.aircraftModelId == id).first()

        if aircraft_model_model is None:
            raise HTTPException(status_code=404, detail='Aircraft Model Not Found.')

        aircraft_model_model.modelName = aircraft_data.modelName

        db.add(aircraft_model_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)
