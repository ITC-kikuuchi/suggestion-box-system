from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp

from database import Base


class Status(Base):
    __tablename__ = "m_status"

    id = Column(Integer, primary_key=True, nullable=False)
    status = Column(String(255), nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)