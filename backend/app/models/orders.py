from uuid import UUID
from datetime import datetime
from enum import Enum

from sqlalchemy import text, Text, DateTime, ForeignKey, UUID as SQLAlchemyUUID, Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.users import User
    
class StatusType(str, Enum):
    PENDING='PENDING'
    PAID='PAID' 
    PROCESSING='PROCESSING'
    SHIPPED='SHIPPED'
    DELIVERED='DELIVERED'
    CANCELLED='CANCELLED'
    
class Order(Base):
    __tablename__ = 'orders'
    
    id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID,
        primary_key=True,
        server_default=text('gen_random_uuid()')
    )
    
    user_id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID,
        ForeignKey('users.id', ondelete=text('CASCADE')),
        nullable=False
    )
    
    status: Mapped[Enum] = mapped_column(
        SQLAlchemyEnum(StatusType, name='status_type', native_enum=True),
        nullable=False
    )
    
    shipping_address: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP')
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text('NOW()'),
        onupdate=text('NOW()')
    )
    
    user: Mapped['User'] = relationship(back_populates='orders')