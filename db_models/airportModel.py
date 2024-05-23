from config.database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class airportModel(Base):
    __tablename__ = 'airport'

    airportId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    airportName = Column(String, nullable=False)

    groundStaff = relationship("groundStaffModel", back_populates="airport")

    # pastStartJourneyDetails = relationship("pastJourneyDetailsModel", back_populates="sourceAirport")
    # pastEndJourneyDetails = relationship("pastJourneyDetailsModel", back_populates="destinationAirports")

    mroVendor = relationship("mroVendorModel", back_populates="airport")
