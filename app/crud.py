from sqlalchemy.orm import Session
from app import models

def create_order(db: Session, order: models.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session):
    return db.query(models.Order).all()