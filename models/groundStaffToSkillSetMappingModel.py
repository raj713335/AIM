from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class groundStaffToSkillSetMappingModel(Base):
    __tablename__ = 'groundStaffToSkillSetMapping'

    skillId = Column(String, ForeignKey("skill.skillId"), nullable=False)
    staffMemberId = Column(String, ForeignKey("groundStaff.staffMemberId"), nullable=False)
