from datetime import datetime
from pydantic import BaseModel, Field



class aircraftImportDisplaySchema(BaseModel):
    aircraftId: str = Field(min_length=3, max_length=50)
    aircraftModelId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)


class repairHistorySchema(BaseModel):
    aircraftId: str = Field(min_length=3, max_length=200)
    durationInHours: int
    startTime: str = Field(min_length=3, max_length=50)
    endTime: str = Field(min_length=3, max_length=50)
    costIncurredInDollars: int
    repairStatus: str = Field(min_length=3, max_length=50)
    repairDescription: str = Field(min_length=3, max_length=50)


class repairHistoryImportDisplaySchema(BaseModel):
    repairInstanceId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=200)
    durationInHours: int
    startTime: datetime
    endTime: datetime
    costIncurredInDollars: int
    repairStatus: str = Field(min_length=3, max_length=50)
    repairDescription: str = Field(min_length=3, max_length=50)


class repairHistoryDisplaySchema(BaseModel):
    repairInstanceId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=200)
    durationInHours: int
    startTime: datetime
    endTime: datetime
    costIncurredInDollars: int
    repairStatus: str = Field(min_length=3, max_length=50)
    repairDescription: str = Field(min_length=3, max_length=50)

    aircraft: aircraftImportDisplaySchema

