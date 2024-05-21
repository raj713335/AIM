from config.database import Base
from sqlalchemy import Column, String, ForeignKey


class damageToPartsMappingModel(Base):
    __tablename__ = 'damageToPartsMapping'

    damageInstanceIf = Column(String, ForeignKey("damage.damageInstanceId"), nullable=False)
    partDamaged = Column(String, ForeignKey("aircraftPart.partId"), nullable=False)
