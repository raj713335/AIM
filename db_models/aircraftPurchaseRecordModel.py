from config.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer


class aircraftPurchaseRecordModel(Base):
    __tablename__ = 'aircraftPurchaseRecord'

    airlineId = Column(String, ForeignKey("airline.airlineId"), primary_key=True, nullable=False)
    aircraftId = Column(String, ForeignKey("aircraft.aircraftId"), primary_key=True, nullable=False)
    price = Column(Integer,  nullable=False)
