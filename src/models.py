from sqlalchemy import Integer, String, BLOB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import Column
from .database import Base
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    username = Column(String, nullable=False)


class Audiofile(Base):
    __tablename__ = "audiofiles"
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    blob = Column(BLOB, nullable=False)
