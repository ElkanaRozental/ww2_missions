from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from config.base import Base


class Priority(Base):
    __tablename__ = "priority"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    missions = relationship(
        "NormalizedMission",
        back_populates="priority",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (f"<Priority(id={self.id}, name={self.name},"
                f"missions={self.missions}>")