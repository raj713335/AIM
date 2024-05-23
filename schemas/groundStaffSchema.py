from datetime import datetime
from pydantic import BaseModel, Field


class airlineImportDisplaySchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    airlineName: str = Field(min_length=3, max_length=50)
    regionOperated: str = Field(min_length=3, max_length=50)
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)


class airportImportDisplaySchema(BaseModel):
    airportId: str = Field(min_length=3, max_length=50)
    airportName: str = Field(min_length=3, max_length=50)


class groundStaffSchema(BaseModel):
    staffMemberFirstName: str = Field(min_length=3, max_length=50)
    staffMemberLastName: str = Field(min_length=3, max_length=50)
    staffMemberDob: str
    employerAirlineId: str = Field(min_length=3, max_length=50)
    deployedAirportId: str = Field(min_length=3, max_length=50)
    # staffMemberUsername: str = Field(min_length=3, max_length=50)
    # staffMemberPassword: str = Field(min_length=3, max_length=50)


class groundStaffImportDisplaySchema(BaseModel):
    staffMemberId: str = Field(min_length=3, max_length=50)
    staffMemberFirstName: str = Field(min_length=3, max_length=50)
    staffMemberLastName: str = Field(min_length=3, max_length=50)
    staffMemberDob: datetime
    employerAirlineId: str = Field(min_length=3, max_length=50)
    deployedAirportId: str = Field(min_length=3, max_length=50)
    # staffMemberUsername: str = Field(min_length=3, max_length=50)
    # staffMemberPassword: str = Field(min_length=3, max_length=50)


class groundStaffDisplaySchema(BaseModel):
    staffMemberId: str = Field(min_length=3, max_length=50)
    staffMemberFirstName: str = Field(min_length=3, max_length=50)
    staffMemberLastName: str = Field(min_length=3, max_length=50)
    staffMemberDob: datetime
    employerAirlineId: str = Field(min_length=3, max_length=50)
    deployedAirportId: str = Field(min_length=3, max_length=50)
    # staffMemberUsername: str = Field(min_length=3, max_length=50)
    # staffMemberPassword: str = Field(min_length=3, max_length=50)

    airline: airlineImportDisplaySchema
    airport: airportImportDisplaySchema
