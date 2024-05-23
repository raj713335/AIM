from datetime import datetime
from pydantic import BaseModel, Field


class aircraftImportDisplaySchema(BaseModel):
    aircraftId: str = Field(min_length=3, max_length=50)
    aircraftModelId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)


class airlineImportDisplaySchema(BaseModel):
    airlineId: str = Field(min_length=3, max_length=50)
    airlineName: str = Field(min_length=3, max_length=50)
    regionOperated: str = Field(min_length=3, max_length=50)
    airlineAdminUsername: str = Field(min_length=3, max_length=20)
    airlineAdminPassword: str = Field(min_length=3, max_length=20)


class airportImportDisplaySchema(BaseModel):
    airportId: str = Field(min_length=3, max_length=50)
    airportName: str = Field(min_length=3, max_length=50)


class pastJourneyDetailsSchema(BaseModel):
    aircraftId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)
    sourceAirportId: str = Field(min_length=3, max_length=50)
    destinationAirport: str = Field(min_length=3, max_length=50)


class pastJourneyDetailsImportDisplaySchema(BaseModel):
    journeyId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)
    sourceAirportId: str = Field(min_length=3, max_length=50)
    destinationAirport: str = Field(min_length=3, max_length=50)


class pastJourneyDetailsDisplaySchema(BaseModel):
    journeyId: str = Field(min_length=3, max_length=50)
    aircraftId: str = Field(min_length=3, max_length=50)
    ownerAirlineId: str = Field(min_length=3, max_length=50)
    sourceAirportId: str = Field(min_length=3, max_length=50)
    destinationAirport: str = Field(min_length=3, max_length=50)

    aircraft: aircraftImportDisplaySchema
    airline: airlineImportDisplaySchema
    # sourceAirport: airportImportDisplaySchema
    # destinationAirports: airportImportDisplaySchema
