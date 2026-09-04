from sqlalchemy import String, Text, text, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from sqlalchemy import UUID as SQLAlchemyUUID
from datetime import datetime

from app.core.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.products import Product

class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID, 
        primary_key=True, 
        server_default=text("gen_random_uuid()")
    )

    category_name: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )
    
    description: Mapped[str] = mapped_column(
        Text, 
        nullable=False
    )
    
    is_active: Mapped[bool] = mapped_column(
        Boolean, 
        nullable=False
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=text("CURRENT_TIMESTAMP")
    )
    
    products: Mapped[list['Product']] = relationship(back_populates='category')
    