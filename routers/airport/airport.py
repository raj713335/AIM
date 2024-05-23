import uuid
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import airportModel
from config.database import SessionLocal
from schemas.airportSchema import airportSchema, airportDisplaySchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/airport',
    tags=['Airport Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_airport_details', response_model=List[airportDisplaySchema], status_code=status.HTTP_200_OK)
async def get_all_airport_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(airportModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.get('/get_airport_details/{id}', response_model=airportDisplaySchema, status_code=status.HTTP_200_OK)
async def get_airport_details(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(airportModel).filter(airportModel.airportId == id).first()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_airport_details", status_code=status.HTTP_201_CREATED)
async def add_airport_details(db: db_dependency, airport_data: airportSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        airport_model = airportModel(
            airportId=uuid.uuid4(),
            airportName=airport_data.airportName
        )

        db.add(airport_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_airport_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_airport_details(db: db_dependency, airport_data: airportSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        airport_model = db.query(airportModel).filter(airportModel.airportId == id).first()

        if airport_model is None:
            raise HTTPException(status_code=404, detail='Airport Not Found.')

        airport_model.airportName = airport_data.airportName

        db.add(airport_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
