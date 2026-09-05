from datetime import datetime
from uuid import UUID
from decimal import Decimal

from sqlalchemy import text, UUID as SQLAlchemyUUID, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.orders import Order
    from app.models.products import Product

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    order_id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID,
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False
    )

    product_id: Mapped[UUID] = mapped_column(
        SQLAlchemyUUID,
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    unit_price: Mapped[Decimal] = mapped_column(
        DECIMAL(10, 2),
        nullable=False
    )

    subtotal: Mapped[Decimal] = mapped_column(
        DECIMAL(10, 2),
        nullable=False
    )

    order: Mapped["Order"] = relationship(
        back_populates="items"
    )

    product: Mapped["Product"] = relationship(
        back_populates="order_items"
    )