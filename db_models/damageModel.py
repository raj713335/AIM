from config.database import Base
from sqlalchemy import Column, String, ForeignKey, Date
from datetime import datetime


class damageModel(Base):
    __tablename__ = 'damage'

    damageInstanceId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    damageDescription = Column(String, nullable=False)
    damageTimestamp = Column(Date, default=datetime.now, nullable=False)
    journeyId = Column(String, ForeignKey("pastJourneyDetails.journeyId"), nullable=False)
    severityOfDamage = Column(String, nullable=False)
    repairInstance = Column(String, ForeignKey("repairHistory.repairInstanceId"), nullable=False)
    currentStatusOfDamage = Column(String, nullable=False)
