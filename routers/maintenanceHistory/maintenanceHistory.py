import uuid
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import maintenanceHistoryModel
from config.database import SessionLocal
from schemas.maintenanceHistorySchema import maintenanceHistorySchema, maintenanceHistoryDisplaySchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/maintenance_history',
    tags=['Maintenance History Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_maintenance_history', response_model=List[maintenanceHistoryDisplaySchema], status_code=status.HTTP_200_OK)
async def get_all_maintenance_history(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(maintenanceHistoryModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.get("/get_maintenance_history/{id}", response_model=maintenanceHistoryDisplaySchema, status_code=status.HTTP_200_OK)
async def get_maintenance_history(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        return db.query(maintenanceHistoryModel).filter(maintenanceHistoryModel.maintenanceId == id).first()

    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_maintenance_history", status_code=status.HTTP_201_CREATED)
async def add_maintenance_history(db: db_dependency, maintenance_history_data: maintenanceHistorySchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        maintenance_history_model = maintenanceHistoryModel(
            maintenanceId=uuid.uuid4(),
            aircraftId=maintenance_history_data.aircraftId,
            responsibleMroId=maintenance_history_data.responsibleMroId,
            maintenanceStatus=maintenance_history_data.maintenanceStatus,
            durationInDays=maintenance_history_data.durationInDays,
            startTime=maintenance_history_data.startTime,
            endTime=maintenance_history_data.endTime,
            costIncurredInDollars=maintenance_history_data.costIncurredInDollars
        )

        db.add(maintenance_history_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_maintenance_history/{id}", status_code=status.HTTP_201_CREATED)
async def update_maintenance_history(db: db_dependency, maintenance_history_data: maintenanceHistorySchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        maintenance_history_model = db.query(maintenanceHistoryModel).filter(maintenanceHistoryModel.maintenanceId == id).first()

        if maintenance_history_model is None:
            return HTTPException(status_code=404, detail='Maintenance History Details Not Found.')

        maintenance_history_model.aircraftId = maintenance_history_data.aircraftId
        maintenance_history_model.responsibleMroId = maintenance_history_data.responsibleMroId
        maintenance_history_model.maintenanceStatus = maintenance_history_data.maintenanceStatus
        maintenance_history_model.durationInDays = maintenance_history_data.durationInDays
        maintenance_history_model.startTime = maintenance_history_data.startTime
        maintenance_history_model.endTime = maintenance_history_data.endTime
        maintenance_history_model.costIncurredInDollars = maintenance_history_data.costIncurredInDollars

        db.add(maintenance_history_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
