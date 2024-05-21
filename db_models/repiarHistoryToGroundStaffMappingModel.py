from config.database import Base
from sqlalchemy import Column, String, Boolean, ForeignKey
from datetime import datetime


class repairHistoryToGroundStaffMappingModel(Base):
    __tablename__ = 'repairHistoryToGroundStaffMapping'

    repairId = Column(String, ForeignKey("repairHistory.repairInstanceId"), primary_key=True, nullable=False)
    groundStaffInvolved = Column(String, ForeignKey("groundStaff.staffMemberId"), primary_key=True, nullable=False)

