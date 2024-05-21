from config.database import Base
from sqlalchemy import Column, String, ForeignKey, Integer, Date
from datetime import datetime


class maintenanceHistoryModel(Base):
    __tablename__ = 'maintenanceHistory'

    maintenanceId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    aircraftId = Column(String, ForeignKey("aircraft.aircraftId"), nullable=False)
    responsibleMroId = Column(String, ForeignKey("mroVendor.mroId"), nullable=False)
    maintenanceStatus = Column(String, nullable=False)
    durationInDays = Column(Integer, nullable=False)
    startTime = Column(Date, default=datetime.now, nullable=False)
    endTime = Column(String, default=datetime.now, nullable=False)
    costIncurredInDollars = Column(Integer, nullable=False)
