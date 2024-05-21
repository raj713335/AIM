from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class damageToPartsMappingModel(Base):
    __tablename__ = 'damageToPartsMapping'

    damageInstanceIf = Column(String, ForeignKey("damage.damageInstanceId"), primary_key=True, nullable=False)
    partDamaged = Column(String, ForeignKey("aircraftPart.partId"), primary_key=True, nullable=False)
