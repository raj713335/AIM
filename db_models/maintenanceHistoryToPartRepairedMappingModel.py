from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class maintenanceHistoryToPartRepairedMappingModel(Base):
    __tablename__ = 'maintenanceHistoryToPartRepairedMapping'

    maintenanceId = Column(String, ForeignKey("maintenanceHistory.maintenanceId"), primary_key=True, nullable=False)
    partRepairedId = Column(String, ForeignKey("aircraftPart.partId"), primary_key=True, nullable=False)
