import uuid
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import groundStaffModel
from config.database import SessionLocal
from schemas.groundStaffSchema import groundStaffSchema, groundStaffDisplaySchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/groundStaff',
    tags=['GroundStaff Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_groundStaff_details', response_model=List[groundStaffDisplaySchema], status_code=status.HTTP_200_OK)
async def get_all_groundStaff_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(groundStaffModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.get('/get_groundStaff_details/{id}', response_model=groundStaffDisplaySchema, status_code=status.HTTP_200_OK)
async def get_groundStaff_details(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(groundStaffModel).filter(groundStaffModel.staffMemberId == id).first()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_groundStaff_details", status_code=status.HTTP_201_CREATED)
async def add_groundStaff_details(db: db_dependency, ground_staff_data: groundStaffSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        airport_model = groundStaffModel(
            staffMemberId=uuid.uuid4(),
            staffMemberFirstName=ground_staff_data.staffMemberFirstName,
            staffMemberLastName=ground_staff_data.staffMemberLastName,
            staffMemberDob=ground_staff_data.staffMemberDob,
            employerAirlineId=ground_staff_data.employerAirlineId,
            deployedAirportId=ground_staff_data.deployedAirportId,
            # staffMemberUsername=ground_staff_data.staffMemberUsername,
            # staffMemberPassword=ground_staff_data.staffMemberPassword,
        )

        db.add(airport_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_groundStaff_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_groundStaff_details(db: db_dependency, ground_staff_data: groundStaffSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        ground_staff_model = db.query(groundStaffModel).filter(groundStaffModel.staffMemberId == id).first()

        if ground_staff_model is None:
            raise HTTPException(status_code=404, detail='Ground Staff Not Found.')

        ground_staff_model.staffMemberFirstName = ground_staff_data.staffMemberFirstName
        ground_staff_model.staffMemberLastName = ground_staff_data.staffMemberLastName
        ground_staff_model.staffMemberDob = ground_staff_data.staffMemberDob
        ground_staff_model.employerAirlineId = ground_staff_data.employerAirlineId
        ground_staff_model.deployedAirportId = ground_staff_data.deployedAirportId
        # ground_staff_model.staffMemberUsername = ground_staff_data.staffMemberUsername
        # ground_staff_model.staffMemberPassword = ground_staff_data.staffMemberPassword

        db.add(ground_staff_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
