from datetime import datetime
from pydantic import BaseModel, Field


class pastJourneyDetailsImportDisplaySchema(BaseModel):
    journeyId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)
    sourceAirportId: str = Field(min_length=3, max_length=50)
    destinationAirport: str = Field(min_length=3, max_length=50)


class repairHistoryImportDisplaySchema(BaseModel):
    repairInstanceId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    durationInHours: int
    startTime: datetime
    endTime: datetime
    costIncurredInDollars: int
    repairStatus: str = Field(min_length=3, max_length=50)
    repairDescription: str = Field(min_length=3, max_length=50)


class damageSchema(BaseModel):
    damageDescription: str = Field(min_length=3, max_length=50)
    damageTimestamp: str = Field(min_length=3, max_length=50)
    journeyId: str = Field(min_length=3, max_length=50)
    severityOfDamage: str = Field(min_length=3, max_length=50)
    repairInstance: str = Field(min_length=3, max_length=50)
    currentStatusOfDamage: str = Field(min_length=3, max_length=50)


class damageImportDisplaySchema(BaseModel):
    damageInstanceId: str = Field(min_length=3, max_length=50)
    damageDescription: str = Field(min_length=3, max_length=50)
    damageTimestamp: datetime
    journeyId: str = Field(min_length=3, max_length=50)
    severityOfDamage: str = Field(min_length=3, max_length=50)
    repairInstance: str = Field(min_length=3, max_length=50)
    currentStatusOfDamage: str = Field(min_length=3, max_length=50)


class damageDisplaySchema(BaseModel):
    damageInstanceId: str = Field(min_length=3, max_length=50)
    damageDescription: str = Field(min_length=3, max_length=50)
    damageTimestamp: datetime
    journeyId: str = Field(min_length=3, max_length=50)
    severityOfDamage: str = Field(min_length=3, max_length=50)
    repairInstance: str = Field(min_length=3, max_length=50)
    currentStatusOfDamage: str = Field(min_length=3, max_length=50)

    pastJourneyDetails: pastJourneyDetailsImportDisplaySchema
    repairHistory: repairHistoryImportDisplaySchema
