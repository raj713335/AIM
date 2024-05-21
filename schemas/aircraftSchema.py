from pydantic import BaseModel, Field


class aircraftSchema(BaseModel):
    modelName: str = Field(min_length=3, max_length=50)


class aircraftPartSchema(BaseModel):
    partName: str = Field(min_length=3, max_length=50)
    aircraftLinkedTo: str = Field(min_length=3, max_length=50)
