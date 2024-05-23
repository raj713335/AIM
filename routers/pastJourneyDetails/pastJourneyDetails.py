import uuid
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import pastJourneyDetailsModel
from config.database import SessionLocal
from schemas.pastJourneyDetailsSchema import pastJourneyDetailsDisplaySchema, pastJourneyDetailsSchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/past_journey_details',
    tags=['Past Journey Details Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_past_journey_details', response_model=List[pastJourneyDetailsDisplaySchema], status_code=status.HTTP_200_OK)
async def get_all_past_journey_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(pastJourneyDetailsModel).all()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.get('/get_past_journey_details/{id}', response_model=pastJourneyDetailsDisplaySchema, status_code=status.HTTP_200_OK)
async def get_past_journey_details(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(pastJourneyDetailsModel).filter(pastJourneyDetailsModel.journeyId == id).first()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post("/add_past_journey_details", status_code=status.HTTP_201_CREATED)
async def add_past_journey_details(db: db_dependency, past_journey_data: pastJourneyDetailsSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        past_journey_model = pastJourneyDetailsModel(
            journeyId=uuid.uuid4(),
            aircraftId=past_journey_data.aircraftId,
            ownerAirlineId=past_journey_data.ownerAirlineId,
            sourceAirportId=past_journey_data.sourceAirportId,
            destinationAirport=past_journey_data.destinationAirport,
        )

        db.add(past_journey_model)
        db.commit()

    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.put("/update_past_journey_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_past_journey_details(db: db_dependency, past_journey_data: pastJourneyDetailsSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        past_journey_model = db.query(pastJourneyDetailsModel).filter(pastJourneyDetailsModel.journeyId == id).first()

        if past_journey_model is None:
            raise HTTPException(status_code=404, detail='Journey Details Not Found.')

        past_journey_model.aircraftId = past_journey_data.aircraftId
        past_journey_model.ownerAirlineId = past_journey_data.ownerAirlineId
        past_journey_model.sourceAirportId = past_journey_data.sourceAirportId
        past_journey_model.destinationAirport = past_journey_data.destinationAirport

        db.add(past_journey_model)
        db.commit()
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)