from config.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class aircraftModel(Base):
    __tablename__ = 'aircraft'

    aircraftId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    aircraftModelId = Column(String, ForeignKey("aircraftModel.aircraftModelId"), unique=True, nullable=False)
    ownerAirlineId = Column(String, ForeignKey("airline.airlineId"), nullable=False)

    aircraftModel = relationship("aircraftModelModel", back_populates="aircraft")
    ownerAirlines = relationship("airlineModel", back_populates="aircraft")
    aircraftPartModel = relationship("aircraftPartModel", back_populates="aircraft")
    aircraftPurchaseRecord = relationship("aircraftPurchaseRecordModel", back_populates="aircraft")
    pastJourneyDetails = relationship("pastJourneyDetailsModel", back_populates="aircraft")
    repairHistory = relationship("repairHistoryModel", back_populates="aircraft")
