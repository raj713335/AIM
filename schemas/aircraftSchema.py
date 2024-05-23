from typing import List
from pydantic import BaseModel, Field
# from schemas.airlineSchema import airlineDisplaySchema


class airlineImportDisplaySchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    airlineName: str = Field(min_length=3, max_length=50)
    regionOperated: str = Field(min_length=3, max_length=50)
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)

class aircraftImportDisplaySchema(BaseModel):
    aircraftId: str = Field(min_length=3, max_length=50)
    aircraftModelId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)


class aircraftModelImportDisplaySchema(BaseModel):
    aircraftModelId: str = Field(min_length=3, max_length=50)
    modelName: str = Field(min_length=3, max_length=50)


class aircraftModelDisplaySchema(BaseModel):
    aircraftModelId: str = Field(min_length=3, max_length=50)
    modelName: str = Field(min_length=3, max_length=50)

    aircraft: List[aircraftImportDisplaySchema] = []


class aircraftModelSchema(BaseModel):
    modelName: str = Field(min_length=3, max_length=50)


class aircraftPartSchema(BaseModel):
    partName: str = Field(min_length=3, max_length=50)
    aircraftLinkedTo: str = Field(min_length=3, max_length=50)


class aircraftPartImportDisplaySchema(BaseModel):
    partId: str = Field(min_length=3, max_length=50)
    partName: str = Field(min_length=3, max_length=50)
    aircraftLinkedTo: str = Field(min_length=3, max_length=50)


class aircraftPartDisplaySchema(BaseModel):
    partId: str = Field(min_length=3, max_length=50)
    partName: str = Field(min_length=3, max_length=50)
    aircraftLinkedTo: str = Field(min_length=3, max_length=50)

    aircraft: aircraftImportDisplaySchema


class aircraftPurchaseRecordSchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    price: int


class aircraftPurchaseRecordImportDisplaySchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    price: int


class aircraftPurchaseRecordDisplaySchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    price: int

    airline: airlineImportDisplaySchema
    aircraft: aircraftImportDisplaySchema


class aircraftSchema(BaseModel):
    aircraftModelId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)


class aircraftDisplaySchema(BaseModel):
    aircraftId: str = Field(min_length=3, max_length=50)
    aircraftModelId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)

    aircraftModel: aircraftModelImportDisplaySchema
    ownerAirlines: airlineImportDisplaySchema
    aircraftPartModel: List[aircraftPartImportDisplaySchema] = []
    aircraftPurchaseRecord: List[aircraftPurchaseRecordImportDisplaySchema] = []
