from pydantic import BaseModel, Field


class airportSchema(BaseModel):
    airportName: str = Field(min_length=3, max_length=10)
