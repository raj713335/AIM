from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class repairHistoryToPartRepairedMappingModel(Base):
    __tablename__ = 'repairHistoryToPartRepairedMapping'

    repairId = Column(String, ForeignKey("repairHistory.repairInstanceId"), primary_key=True, unique=True, nullable=False, index=True)
    partRepairedId = Column(String, ForeignKey("aircraftPart.partId"), nullable=False)
