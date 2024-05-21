from config.database import Base
from sqlalchemy import Column, String


class skillModel(Base):
    __tablename__ = 'skill'

    skillId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    skillName = Column(String, nullable=False)
