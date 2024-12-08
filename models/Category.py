from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = "m_category"

    id = Column(Integer, primary_key=True, nullable=False)
    category = Column(String(255), nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)

    suggestionCategory = relationship("SuggestionCategory", back_populates="category")
