from config.database import Base
from sqlalchemy import Column, String


class aircraftModelModel(Base):
    __tablename__ = 'aircraftModel'

    aircraftModelId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    modelName = Column(String, nullable=False)
