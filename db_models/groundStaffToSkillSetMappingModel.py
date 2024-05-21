from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class groundStaffToSkillSetMappingModel(Base):
    __tablename__ = 'groundStaffToSkillSetMapping'

    skillId = Column(String, ForeignKey("skill.skillId"), primary_key=True, nullable=False)
    staffMemberId = Column(String, ForeignKey("groundStaff.staffMemberId"), primary_key=True, nullable=False)
