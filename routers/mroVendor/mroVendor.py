import uuid
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Path
from starlette import status
from db_models import mroVendorModel
from config.database import SessionLocal
from schemas.mroVendorSchema import mroVendorSchema, mroVendorDisplaySchema
from ..auth import get_user_info
from schemas.userPayload import userPayload

router = APIRouter(
    prefix='/mroVendor',
    tags=['MRO Vendor Details']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_all_mroVendor_details', response_model=List[mroVendorDisplaySchema], status_code=status.HTTP_200_OK)
async def get_all_mroVendor_details(db: db_dependency):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')
        return db.query(mroVendorModel).all()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.get("/get_mroVendor_details/{id}", response_model=mroVendorDisplaySchema, status_code=status.HTTP_200_OK)
async def get_mroVendor_details(db: db_dependency, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        return db.query(mroVendorModel).filter(mroVendorModel.mroId == id).first()

    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.post("/add_mroVendor_details", status_code=status.HTTP_201_CREATED)
async def add_mroVendor_details(db: db_dependency, mro_vendor_data: mroVendorSchema):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        mro_vendor_model = mroVendorModel(
            mroId=uuid.uuid4(),
            mroCompanyName=mro_vendor_data.mroCompanyName,
            mroAirportId=mro_vendor_data.mroAirportId
        )

        db.add(mro_vendor_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)


@router.put("/update_mroVendor_details/{id}", status_code=status.HTTP_201_CREATED)
async def update_mroVendor_details(db: db_dependency, mro_vendor_model_data: mroVendorSchema, id: str = Path):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication failed')
        mro_vendor_model = db.query(mroVendorModel).filter(mroVendorModel.mroId == id).first()

        if mro_vendor_model is None:
            return HTTPException(status_code=404, detail='Airline Not Found.')

        mro_vendor_model.mroCompanyName = mro_vendor_model_data.mroCompanyName
        mro_vendor_model.mroAirportId = mro_vendor_model_data.mroAirportId

        db.add(mro_vendor_model)
        db.commit()
    except Exception as err:
        return HTTPException(status_code=401, detail=err)
