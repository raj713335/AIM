import uuid
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import damageModel
from config.database import SessionLocal
from schemas.damageSchema import damageSchema, damageDisplaySchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/damage',
    tags=['Damage Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_damage_details', response_model=List[damageDisplaySchema], status_code=status.HTTP_200_OK)
async def get_all_damage_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(damageModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.get("/get_damage_details/{id}", response_model=damageDisplaySchema, status_code=status.HTTP_200_OK)
async def get_damage_details(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        return db.query(damageModel).filter(damageModel.damageInstanceId == id).first()

    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_damage_details", status_code=status.HTTP_201_CREATED)
async def add_damage_details(db: db_dependency, damage_data: damageSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        damage_model = damageModel(
            damageInstanceId=uuid.uuid4(),
            damageDescription=damage_data.damageDescription,
            damageTimestamp=damage_data.damageTimestamp,
            journeyId=damage_data.journeyId,
            severityOfDamage=damage_data.severityOfDamage,
            repairInstance=damage_data.repairInstance,
            currentStatusOfDamage=damage_data.currentStatusOfDamage
        )

        db.add(damage_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_damage_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_damage_details(db: db_dependency, damage_data: damageSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        damage_model = db.query(damageModel).filter(damageModel.damageInstanceId == id).first()

        if damage_model is None:
            return HTTPException(status_code=404, detail='Damage details Not Found.')

        damage_model.damageDescription = damage_data.damageDescription
        damage_model.damageTimestamp = damage_data.damageTimestamp
        damage_model.journeyId = damage_data.journeyId
        damage_model.severityOfDamage = damage_data.severityOfDamage
        damage_model.repairInstance = damage_data.repairInstance
        damage_model.currentStatusOfDamage = damage_data.currentStatusOfDamage

        db.add(damage_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
