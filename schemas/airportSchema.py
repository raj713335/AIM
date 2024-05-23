from typing import List
from pydantic import BaseModel, Field
from schemas.groundStaffSchema import groundStaffImportDisplaySchema


class airportSchema(BaseModel):
    airportName: str = Field(min_length=3, max_length=50)


class airportImportDisplaySchema(BaseModel):
    airportId: str = Field(min_length=3, max_length=50)
    airportName: str = Field(min_length=3, max_length=50)


class airportDisplaySchema(BaseModel):
    airportId: str = Field(min_length=3, max_length=50)
    airportName: str = Field(min_length=3, max_length=50)

    groundStaff: List[groundStaffImportDisplaySchema] = []
