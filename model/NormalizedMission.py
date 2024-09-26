from sqlalchemy import Integer, Column, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base


class NormalizedMission(Base):
    __tablename__ = "normalized_mission"
    id = Column(Integer, primary_key=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    target_type_id = Column(Integer, ForeignKey("target_type.id"), nullable=False)
    target_industry_id = Column(Integer, ForeignKey("target_industry.id"), nullable=False)
    priority_id = Column(Integer, ForeignKey("priority.id"), nullable=False)

    country = relationship("Country", back_populates="missions")
    city = relationship("City", back_populates="missions")
    location = relationship("Location", back_populates="missions")
    type = relationship("TargetType", back_populates="missions")
    industry = relationship("TargetIndustry", back_populates="missions")
    priority = relationship("Priority", back_populates="missions")

