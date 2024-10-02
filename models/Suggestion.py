from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class Suggestion(Base):
    __tablename__ = "t_suggestion"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    contents = Column(Text, nullable=False)
    status_id = Column(Integer, ForeignKey("m_status.id"), nullable=False, default=1)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)


    suggestionCategory = relationship("SuggestionCategory", back_populates="suggestion")
    suggestionComment = relationship("SuggestionComment", back_populates="suggestion")
    suggestionFavorite = relationship("SuggestionFavorite", back_populates="suggestion")