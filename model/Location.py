from sqlalchemy import Integer, Column, String, DECIMAL
from sqlalchemy.orm import relationship

from config.base import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(DECIMAL, nullable=False)
    longitude = Column(DECIMAL, nullable=False)
    missions = relationship(
        "Mission",
        secondary="normalized_mission",
        back_populates="location",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (f"<Location(id={self.id}, latitude={self.latitude}, longitude={self.longitude}"
                f"missions={self.missions}>")