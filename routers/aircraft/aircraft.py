import uuid
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import aircraftModelModel, aircraftPartModel
from config.database import SessionLocal
from schemas.aircraftSchema import aircraftSchema, aircraftPartSchema
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


# Aircraft Model


@router.get('/get_all_aircraft_model', status_code=status.HTTP_200_OK)
async def get_all_aircraft(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(aircraftModelModel).all()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.get('/get_aircraft_model/{id}', status_code=status.HTTP_200_OK)
async def get_aircraft(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(aircraftModelModel).filter(aircraftModelModel.aircraftModelId == id).first()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/add_aircraft_model", status_code=status.HTTP_201_CREATED)
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


@router.put("/update_aircraft_model/{id}", status_code=status.HTTP_201_CREATED)
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


@router.get('/get_all_aircraft_part', status_code=status.HTTP_200_OK)
async def get_all_aircraft_part(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(aircraftPartModel).all()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.get('/get_aircraft_part/{id}', status_code=status.HTTP_200_OK)
async def get_aircraft_part(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(aircraftPartModel).filter(aircraftPartModel.partId == id).first()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/add_aircraft_part", status_code=status.HTTP_201_CREATED)
async def add_aircraft_part(db: db_dependency, aircraft_part_data: aircraftPartSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        aircraft_part_model = aircraftPartModel(
            partId=uuid.uuid4(),
            partName=aircraft_part_data.partName,
            aircraftLinkedTo=aircraftPartSchema.aircraftLinkedTo
        )

        db.add(aircraft_part_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.put("/update_aircraft_part/{id}", status_code=status.HTTP_201_CREATED)
async def update_aircraft_part(db: db_dependency, aircraft_part_data: aircraftPartSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        aircraft_part_model = db.query(aircraftPartModel).filter(aircraftPartModel.partId == id).first()

        if aircraft_part_model is None:
            raise HTTPException(status_code=404, detail='Aircraft Model Not Found.')

        aircraft_part_model.partName = aircraft_part_data.partName
        aircraft_part_model.aircraftLinkedTo = aircraft_part_data.aircraftLinkedTo

        db.add(aircraft_part_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)
