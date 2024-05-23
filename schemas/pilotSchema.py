from datetime import datetime
from pydantic import BaseModel, Field


class airlineImportDisplaySchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    airlineName: str = Field(min_length=3, max_length=50)
    regionOperated: str = Field(min_length=3, max_length=50)
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)


class pilotSchema(BaseModel):
    pilotFirstName: str = Field(min_length=3, max_length=50)
    pilotLastName: str = Field(min_length=3, max_length=50)
    pilotDob: str
    employerAirlineId: str = Field(min_length=3, max_length=50)


class pilotImportDisplaySchema(BaseModel):
    pilotId: str = Field(min_length=3, max_length=50)
    pilotFirstName: str = Field(min_length=3, max_length=50)
    pilotLastName: str = Field(min_length=3, max_length=50)
    pilotDob: datetime
    employerAirlineId: str = Field(min_length=3, max_length=50)


class pilotDisplaySchema(BaseModel):
    pilotId: str = Field(min_length=3, max_length=50)
    pilotFirstName: str = Field(min_length=3, max_length=50)
    pilotLastName: str = Field(min_length=3, max_length=50)
    pilotDob: datetime
    employerAirlineId: str = Field(min_length=3, max_length=50)

    airline: airlineImportDisplaySchema
