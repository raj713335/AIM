from config.database import Base
from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class groundStaffModel(Base):
    __tablename__ = 'groundStaff'

    staffMemberId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    staffMemberFirstName = Column(String, nullable=False)
    staffMemberLastName = Column(String, nullable=False)
    staffMemberDob = Column(Date, unique=True, nullable=False)
    employerAirlineId = Column(String, ForeignKey("airline.airlineId"), nullable=False)
    deployedAirportId = Column(String, ForeignKey("airport.airportId"), nullable=False)

    airline = relationship("airlineModel", back_populates="groundStaff")
    airport = relationship("airportModel", back_populates="groundStaff")
