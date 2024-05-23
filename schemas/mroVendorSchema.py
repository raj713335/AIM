from typing import List
from pydantic import BaseModel, Field


class airportImportDisplaySchema(BaseModel):
    airportId: str = Field(min_length=3, max_length=50)
    airportName: str = Field(min_length=3, max_length=50)


class mroVendorSchema(BaseModel):
    mroCompanyName: str = Field(min_length=3, max_length=50)
    mroAirportId: str = Field(min_length=3, max_length=50)


class mroVendorImportDisplaySchema(BaseModel):
    mroId: str = Field(min_length=3, max_length=50)
    mroCompanyName: str = Field(min_length=3, max_length=50)
    mroAirportId: str = Field(min_length=3, max_length=50)


class mroVendorDisplaySchema(BaseModel):
    mroId: str = Field(min_length=3, max_length=50)
    mroCompanyName: str = Field(min_length=3, max_length=50)
    mroAirportId: str = Field(min_length=3, max_length=50)

    airport: airportImportDisplaySchema
