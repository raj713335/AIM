from config.database import Base
from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class pilotModel(Base):
    __tablename__ = 'pilot'

    pilotId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    pilotFirstName = Column(String, nullable=False)
    pilotLastName = Column(String, nullable=False)
    pilotDob = Column(Date, unique=True, nullable=False)
    employerAirlineId = Column(String, ForeignKey("airline.airlineId"), nullable=False)

    airline = relationship("airlineModel", back_populates="pilot")
