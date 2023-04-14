from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.types import DateTime, Integer

from src.database import Base


class SimpleBaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __str__(self) -> str:
        return f"<SimpleBaseModel {self.id}>"


class BaseModel(SimpleBaseModel):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __str__(self) -> str:
        return f"<BaseModel {self.id}>"
