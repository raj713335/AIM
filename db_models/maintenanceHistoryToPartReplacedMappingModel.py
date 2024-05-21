from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class maintenanceHistoryToPartReplacedMappingModel(Base):
    __tablename__ = 'maintenanceHistoryToPartReplacedMapping'

    maintenanceId = Column(String, ForeignKey("maintenanceHistory.maintenanceId"), primary_key=True, nullable=False)
    partReplacedId = Column(String, ForeignKey("aircraftPart.partId"), primary_key=True, nullable=False)
