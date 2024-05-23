from config.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class pastJourneyDetailsModel(Base):
    __tablename__ = 'pastJourneyDetails'

    journeyId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    aircraftId = Column(String, ForeignKey("aircraft.aircraftId"), nullable=False)
    ownerAirlineId = Column(String, ForeignKey("airline.airlineId"), nullable=False)
    sourceAirportId = Column(String, ForeignKey("airport.airportId"), nullable=False)
    destinationAirport = Column(String, ForeignKey("airport.airportId"), nullable=False)

    aircraft = relationship("aircraftModel", back_populates="pastJourneyDetails")
    airline = relationship("airlineModel", back_populates="pastJourneyDetails")
    # sourceAirport = relationship("airportModel", back_populates="pastStartJourneyDetails")
    # destinationAirports = relationship("airportModel", back_populates="pastEndJourneyDetails")

    damage = relationship("damageModel", back_populates="pastJourneyDetails")


