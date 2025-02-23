from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from app.database import Base

# SQLAlchemy model for DB
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    order_type = Column(String)

# Pydantic model for request/response validation
class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

class OrderResponse(OrderCreate):
    id: int

    class Config:
        orm_mode = True