from config.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer


class aircraftPurchaseRecordModel(Base):
    __tablename__ = 'aircraftPurchaseRecord'

    airlineId = Column(String, ForeignKey("airline.airlineId"), nullable=False)
    aircraftId = Column(String, ForeignKey("aircraft.aircraftId"), nullable=False)
    price = Column(Integer,  nullable=False)
