from config.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class aircraftPartModel(Base):
    __tablename__ = 'aircraftPart'

    partId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    partName = Column(String, nullable=False)
    aircraftLinkedTo = Column(String, ForeignKey("aircraft.aircraftModelId"), nullable=False)

    aircraft = relationship("aircraftModel", back_populates="aircraftPartModel")
