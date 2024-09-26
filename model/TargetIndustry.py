from sqlalchemy import Integer, Column, String, DECIMAL
from sqlalchemy.orm import relationship

from config.base import Base


class TargetIndustry(Base):
    __tablename__ = "target_industry"
    id = Column(Integer, primary_key=True, autoincrement=True)
    industry = Column(String(400), nullable=False)
    missions = relationship(
        "Mission",
        secondary="normalized_mission",
        back_populates="industry",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (f"<TargetIndustry(id={self.id}, industry={self.industry}"
                f"missions={self.missions}>")