from config.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class mroVendorModel(Base):
    __tablename__ = 'mroVendor'

    mroId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    mroCompanyName = Column(String, nullable=False)
    mroAirportId = Column(String, ForeignKey("airport.airportId"), nullable=False)

    airport = relationship("airportModel", back_populates="mroVendor")
    maintenanceHistory = relationship("maintenanceHistoryModel", back_populates="mroVendor")
