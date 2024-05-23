import uuid
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import repairHistoryModel
from config.database import SessionLocal
from schemas.repairHistorySchema import repairHistorySchema, repairHistoryDisplaySchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/repair_history',
    tags=['Repair History Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_repair_history_details', response_model=List[repairHistoryDisplaySchema], status_code=status.HTTP_200_OK)
async def get_all_repair_history_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(repairHistoryModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.get("/get_repair_history_details/{id}", response_model=repairHistoryDisplaySchema, status_code=status.HTTP_200_OK)
async def get_repair_history_details(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        return db.query(repairHistoryModel).filter(repairHistoryModel.repairInstanceId == id).first()

    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_repair_history_details", status_code=status.HTTP_201_CREATED)
async def add_repair_history_details(db: db_dependency, repair_history_data: repairHistorySchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        repair_history_model = repairHistoryModel(
            repairInstanceId=uuid.uuid4(),
            aircraftId=repair_history_data.aircraftId,
            durationInHours=repair_history_data.durationInHours,
            startTime=repair_history_data.startTime,
            endTime=repair_history_data.endTime,
            costIncurredInDollars=repair_history_data.costIncurredInDollars,
            repairStatus=repair_history_data.repairStatus,
            repairDescription=repair_history_data.repairDescription,
        )

        db.add(repair_history_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_repair_history_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_repair_history_details(db: db_dependency, repair_history_data: repairHistorySchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        repair_history_model = db.query(repairHistoryModel).filter(repairHistoryModel.repairInstanceId == id).first()

        if repair_history_model is None:
            return HTTPException(status_code=404, detail='Repair History Not Found.')

        repair_history_model.aircraftId = repair_history_data.aircraftId
        repair_history_model.durationInHours = repair_history_data.durationInHours
        repair_history_model.startTime = repair_history_data.startTime
        repair_history_model.endTime = repair_history_data.endTime
        repair_history_model.costIncurredInDollars = repair_history_data.costIncurredInDollars
        repair_history_model.repairStatus = repair_history_data.repairStatus
        repair_history_model.repairDescription = repair_history_data.repairDescription

        db.add(repair_history_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
