from pydantic import BaseModel, Field


class sellAircraftSchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    price: int = Field(gt=0)
