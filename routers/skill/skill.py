import uuid
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import skillModel
from config.database import SessionLocal
from schemas.skillSchema import skillSchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/skill',
    tags=['Skill Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_skill_details', status_code=status.HTTP_200_OK)
async def get_all_skill_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(skillModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.get('/get_skill_details/{id}', status_code=status.HTTP_200_OK)
async def get_skill_details(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(skillModel).filter(skillModel.skillId == id).first()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_skill_details", status_code=status.HTTP_201_CREATED)
async def add_skill_details(db: db_dependency, skill_data: skillSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        skill_model = skillModel(
            skillId=uuid.uuid4(),
            skillName=skill_data.skillName
        )

        db.add(skill_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_skill_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_skill_details(db: db_dependency, skill_data: skillSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        skill_model = db.query(skillModel).filter(skillModel.skillId == id).first()

        if skill_model is None:
            raise HTTPException(status_code=404, detail='Airport Not Found.')

        skill_model.skillName = skill_data.skillName

        db.add(skill_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
