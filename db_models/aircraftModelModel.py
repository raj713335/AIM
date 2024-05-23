from config.database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class aircraftModelModel(Base):
    __tablename__ = 'aircraftModel'

    aircraftModelId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    modelName = Column(String, nullable=False)

    aircraft = relationship("aircraftModel", back_populates="aircraftModel")
