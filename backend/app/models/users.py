from sqlalchemy import String, Text, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from uuid import UUID
from sqlalchemy import UUID as SQLAlchemyUUID
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum

from app.core.database import Base

class Role(str, Enum):
    CUSTOMER = "CUSTOMER"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__  = "users"
    
    id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID, 
        primary_key=True, 
        server_default=text("gen_random_uuid()")
    )
    
    username: Mapped[str] = mapped_column(
        String(50), 
        nullable=False, 
        unique=True
    )
    
    email: Mapped[str] = mapped_column(
        String(255), 
        nullable=False, 
        unique=True
    )
    
    password_hash: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )
    
    role: Mapped[Role] = mapped_column(
        SQLAlchemyEnum(Role, name='role_type'), 
        nullable=False
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=text("CURRENT_TIMESTAMP")
    )
    