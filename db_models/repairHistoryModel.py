from config.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer, Date
from datetime import datetime


class repairHistoryModel(Base):
    __tablename__ = 'repairHistory'

    repairInstanceId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    aircraftId = Column(String, ForeignKey("aircraft.aircraftId"), nullable=False)
    durationInHours = Column(Integer, nullable=False)
    startTime = Column(Date, default=datetime.now, nullable=False)
    endTime = Column(Date, default=datetime.now, nullable=False)
    costIncurredInDollars = Column(Integer, nullable=False)
    repairStatus = Column(String, nullable=False)
    repairDescription = Column(String, nullable=False)
