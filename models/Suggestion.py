from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship

from database import Base


class Suggestion(Base):
    __tablename__ = "t_suggestion"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    contents = Column(Text, nullable=False)
    is_resolved = Column(Boolean, nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)
    
    suggestionCategory = relationship("suggestionCategory", back_populates="user")
    suggestionComment = relationship("suggestionComment", back_populates="user")
    suggestionFavorite = relationship("suggestionFavorite", back_populates="user")