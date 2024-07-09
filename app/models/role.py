from app.database import db
from sqlalchemy.orm import Mapped, mapped_column
from typing import List


CUSTOMER_ROLES = [(1, "admin"), (2, 'Buyer'), (3, 'Seller')]


class Role(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    customers: Mapped[List["Customer"]] = db.relationship(back_populates='role')

