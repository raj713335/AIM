import uuid
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import airlineModel
from config.database import SessionLocal
from schemas.airlineSchema import airlineSchema, validate_airlineSchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/airline',
    tags=['Airline Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_airline_details', status_code=status.HTTP_200_OK)
async def get_all_airline_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(airlineModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/validate_airline_details", status_code=status.HTTP_200_OK)
async def validate_airline_details(db: db_dependency, airline_data: validate_airlineSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        airline_model = (
            db.query(airlineModel).filter(airlineModel.airlineAdminUsername == airline_data.airlineAdminUsername)
            .filter(airlineModel.airlineAdminPassword == airline_data.airlineAdminPassword).first())

        if airline_model is None:
            return HTTPException(status_code=404, detail='Invalid Credentials')
        else:
            return airline_model

    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_airline_details", status_code=status.HTTP_201_CREATED)
async def add_airline_details(db: db_dependency, airline_data: airlineSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        airline_model = airlineModel(
            airlineId=uuid.uuid4(),
            airlineName=airline_data.airlineName,
            regionOperated=airline_data.regionOperated,
            airlineAdminUsername=airline_data.airlineAdminUsername,
            airlineAdminPassword=airline_data.airlineAdminPassword,
        )

        db.add(airline_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_airline_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_airline_details(db: db_dependency, airline_data: airlineSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        airline_model = db.query(airlineModel).filter(airlineModel.airlineId == id).first()

        if airline_model is None:
            return HTTPException(status_code=404, detail='Airline Not Found.')

        airline_model.airlineName = airline_data.airlineName
        airline_model.regionOperated = airline_data.regionOperated
        airline_model.airlineAdminUsername = airline_data.airlineAdminUsername
        airline_model.airlineAdminPassword = airline_data.airlineAdminPassword

        db.add(airline_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
