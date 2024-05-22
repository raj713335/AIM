from pydantic import BaseModel, Field


class airlineSchema(BaseModel):
    airlineName: str = Field(min_length=3, max_length=50)
    regionOperated: str = Field(min_length=3, max_length=50)
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)


class validate_airlineSchema(BaseModel):
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)
