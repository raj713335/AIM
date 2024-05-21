from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class repairHistoryToPartReplacedMappingModel(Base):
    __tablename__ = 'repairHistoryToPartReplacedMapping'

    repairId = Column(String, ForeignKey("repairHistory.repairInstanceId"), nullable=False)
    groundStaffInvolved = Column(String, ForeignKey("aircraftPart.partId"), nullable=False)
