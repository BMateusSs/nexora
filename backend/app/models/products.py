from datetime import datetime
from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (text,
                        Text, 
                        String, 
                        DateTime, 
                        Integer, 
                        DECIMAL, 
                        Boolean, 
                        UUID as SQLAlchemyUUID,
                        ForeignKey
                        )
from app.core.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.categories import Category

class Product(Base):
    __tablename__ = 'products'
    
    id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID,
        primary_key=True,
        server_default=text('gen_random_uuid()')
    )
    
    category_id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID,
        ForeignKey('categories.id'),
        nullable=False
    )
    
    product_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False, 
    )
    
    price: Mapped[float] = mapped_column(
        DECIMAL(10, 2),
        nullable=False
    )
    
    stock: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    
    sku: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True
    )
    
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text('CURRENT_TIMESTAMP')
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("NOW()"),
        onupdate=text("NOW()"),
    )
    
    category: Mapped['Category'] = relationship(back_populates='products')
    
    
