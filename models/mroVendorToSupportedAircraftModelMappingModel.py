from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class mroVendorToSupportedAircraftModelMappingModel(Base):
    __tablename__ = 'mroVendorToSupportedAircraftModelMapping'

    aircraftModelId = Column(String, ForeignKey("aircraftModel.aircraftModelId"), nullable=False)
    mroVendorId = Column(String, ForeignKey("mroVendor.mroId"), nullable=False)
