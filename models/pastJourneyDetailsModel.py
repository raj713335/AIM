from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class pastJourneyDetailsModel(Base):
    __tablename__ = 'pastJourneyDetails'

    journeyId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    aircraftId = Column(String, ForeignKey("aircraft.aircraftId"), nullable=False)
    ownerAirlineId = Column(String, ForeignKey("airline.airlineId"), nullable=False)
    sourceAirportId = Column(String, ForeignKey("airport.airportId"), nullable=False)
    destinationAirport = Column(String, ForeignKey("Airport.airportId"), nullable=False)
