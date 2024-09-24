from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp

from database import Base


class User(Base):
    __tablename__ = "m_user"

    id = Column(Integer, primary_key=True, nullable=False)
    mail_address = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    unknown = Column(String(255), nullable=False)
    created_id = Column(Integer)
    updated_id = Column(Integer)
    created_at = Column(Timestamp)
    updated_at = Column(Timestamp)
