from config.database import Base
from sqlalchemy import Column, String


class airlineModel(Base):
    __tablename__ = 'airline'

    airlineId = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    airlineName = Column(String, nullable=False)
    regionOperated = Column(String, nullable=False)
    airlineAdminUsername = Column(String, unique=True, nullable=False)
    airlineAdminPassword = Column(String, nullable=False)
