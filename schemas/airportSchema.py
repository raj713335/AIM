from typing import List
from pydantic import BaseModel, Field
from schemas.groundStaffSchema import groundStaffImportDisplaySchema
from schemas.mroVendorSchema import mroVendorImportDisplaySchema
from schemas.pastJourneyDetailsSchema import pastJourneyDetailsImportDisplaySchema


class airportSchema(BaseModel):
    airportName: str = Field(min_length=3, max_length=50)


class airportImportDisplaySchema(BaseModel):
    airportId: str = Field(min_length=3, max_length=50)
    airportName: str = Field(min_length=3, max_length=50)


class airportDisplaySchema(BaseModel):
    airportId: str = Field(min_length=3, max_length=50)
    airportName: str = Field(min_length=3, max_length=50)

    groundStaff: List[groundStaffImportDisplaySchema] = []
    mroVendor: List[mroVendorImportDisplaySchema] = []
    # pastStartJourneyDetails: List[pastJourneyDetailsImportDisplaySchema] = []
    # pastEndJourneyDetails: List[pastJourneyDetailsImportDisplaySchema] = []
