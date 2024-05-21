from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class aircraftModel(Base):
    __tablename__ = 'aircraft'

    aircraftId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    aircraftModelId = Column(String, ForeignKey("aircraftModel.aircraftModelId"), unique=True, nullable=False)
    ownerAirlineId = Column(String, ForeignKey("airline.airlineId"), nullable=False)
