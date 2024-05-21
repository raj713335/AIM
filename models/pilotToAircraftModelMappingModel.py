from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class pilotToAircraftModelMappingModel(Base):
    __tablename__ = 'pilotToAircraftModelMapping'

    pilotId = Column(String, ForeignKey("pilot.pilotId"), nullable=False)
    modelId = Column(String, ForeignKey("aircraftModel.aircraftModelId"), nullable=False)
