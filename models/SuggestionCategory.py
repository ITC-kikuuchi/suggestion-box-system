from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class SuggestionCategory(Base):
    __tablename__ = "t_suggestion_category"

    id = Column(Integer, primary_key=True, nullable=False)
    suggestion_id = Column(Integer, ForeignKey("t_suggestion.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("m_category.id"), nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)

    suggestion = relationship("Suggestion", back_populates="suggestionCategory")
    category = relationship("Category", back_populates="suggestionCategory")
