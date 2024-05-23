import uuid
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import pilotModel
from config.database import SessionLocal
from schemas.pilotSchema import pilotDisplaySchema, pilotSchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/pilot',
    tags=['Pilot Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_pilot_details', response_model=List[pilotDisplaySchema], status_code=status.HTTP_200_OK)
async def get_all_pilot_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(pilotModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.get('/get_pilot_details/{id}', response_model=pilotDisplaySchema, status_code=status.HTTP_200_OK)
async def get_pilot_details(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(pilotModel).filter(pilotModel.pilotId == id).first()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_pilot_details", status_code=status.HTTP_201_CREATED)
async def add_pilot_details(db: db_dependency, pilot_data: pilotSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        pilot_model = pilotModel(
            pilotId=uuid.uuid4(),
            pilotFirstName=pilot_data.pilotFirstName,
            pilotLastName=pilot_data.pilotLastName,
            pilotDob=pilot_data.pilotDob,
            employerAirlineId=pilot_data.employerAirlineId,
        )

        db.add(pilot_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_pilot_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_pilot_details(db: db_dependency, pilot_data: pilotSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        pilot_model = db.query(pilotModel).filter(pilotModel.pilotId == id).first()

        if pilot_model is None:
            raise HTTPException(status_code=404, detail='Pilot Not Found.')

        pilot_model.pilotFirstName = pilot_data.pilotFirstName
        pilot_model.pilotLastName = pilot_data.pilotLastName
        pilot_model.pilotDob = pilot_data.pilotDob
        pilot_model.employerAirlineId = pilot_data.employerAirlineId

        db.add(pilot_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
