from config.database import Base
from sqlalchemy import Column, String, Boolean, ForeignKey
from datetime import datetime


class repairHistoryToGroundStaffMappingModel(Base):
    __tablename__ = 'repairHistoryToGroundStaffMapping'

    repairId = Column(String, ForeignKey("repairHistory.repairInstanceId"), nullable=False)
    groundStaffInvolved = Column(String, ForeignKey("groundStaff.staffMemberId"), nullable=False)

