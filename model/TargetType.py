from sqlalchemy import Integer, Column, String, DECIMAL
from sqlalchemy.orm import relationship

from config.base import Base


class TargetType(Base):
    __tablename__ = "target_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(400), nullable=False)
    missions = relationship(
        "NormalizedMission",
        back_populates="type",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (f"<TargetType(id={self.id}, type={self.type}"
                f"missions={self.missions}>")