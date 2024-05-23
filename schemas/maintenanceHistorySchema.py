from typing import List
from datetime import datetime
from pydantic import BaseModel, Field


class aircraftImportDisplaySchema(BaseModel):
    aircraftId: str = Field(min_length=3, max_length=50)
    aircraftModelId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)


class mroVendorImportDisplaySchema(BaseModel):
    mroId: str = Field(min_length=3, max_length=50)
    mroCompanyName: str = Field(min_length=3, max_length=50)
    mroAirportId: str = Field(min_length=3, max_length=50)


class maintenanceHistorySchema(BaseModel):
    aircraftId: str = Field(min_length=3, max_length=50)
    responsibleMroId: str = Field(min_length=3, max_length=50)
    maintenanceStatus: str = Field(min_length=3, max_length=50)
    durationInDays: int
    startTime: str = Field(min_length=3, max_length=50)
    endTime: str = Field(min_length=3, max_length=50)
    costIncurredInDollars: int


class maintenanceHistoryImportDisplaySchema(BaseModel):
    maintenanceId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    responsibleMroId: str = Field(min_length=3, max_length=50)
    maintenanceStatus: str = Field(min_length=3, max_length=50)
    durationInDays: int
    startTime: datetime
    endTime: str = Field(min_length=3, max_length=50)
    costIncurredInDollars: int


class maintenanceHistoryDisplaySchema(BaseModel):
    maintenanceId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    responsibleMroId: str = Field(min_length=3, max_length=50)
    maintenanceStatus: str = Field(min_length=3, max_length=50)
    durationInDays: int
    startTime: datetime
    endTime: str = Field(min_length=3, max_length=50)
    costIncurredInDollars: int

    aircraft: aircraftImportDisplaySchema
    mroVendor: mroVendorImportDisplaySchema

