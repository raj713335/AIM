from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class pilotToAircraftModelMappingModel(Base):
    __tablename__ = 'pilotToAircraftModelMapping'

    pilotId = Column(String, ForeignKey("pilot.pilotId"), primary_key=True, nullable=False)
    modelId = Column(String, ForeignKey("aircraftModel.aircraftModelId"), primary_key=True, nullable=False)
