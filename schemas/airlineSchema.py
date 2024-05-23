from typing import List
from pydantic import BaseModel, Field
from schemas.aircraftSchema import aircraftImportDisplaySchema, aircraftPurchaseRecordImportDisplaySchema
from schemas.pilotSchema import pilotImportDisplaySchema


class airlineSchema(BaseModel):
    airlineName: str = Field(min_length=3, max_length=50)
    regionOperated: str = Field(min_length=3, max_length=50)
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)


class airlineImportDisplaySchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    airlineName: str = Field(min_length=3, max_length=50)
    regionOperated: str = Field(min_length=3, max_length=50)
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)


class airlineDisplaySchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    airlineName: str = Field(min_length=3, max_length=50)
    regionOperated: str = Field(min_length=3, max_length=50)
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)

    aircraft: List[aircraftImportDisplaySchema] = []
    aircraftPurchaseRecord: List[aircraftPurchaseRecordImportDisplaySchema] = []
    pilot: List[pilotImportDisplaySchema] = []


class validate_airlineSchema(BaseModel):
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)
