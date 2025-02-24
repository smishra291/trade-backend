from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, crud, database
from fastapi import WebSocket

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"message": " Deployed via CI/CD!"}

@app.post("/orders", response_model=models.OrderResponse)
def create_order(order: models.OrderCreate, db: Session = Depends(database.get_db)):
    return crud.create_order(db=db, order=order)

@app.get("/orders", response_model=List[models.OrderResponse])
def read_orders(db: Session = Depends(database.get_db)):
    return crud.get_orders(db=db)

@app.websocket("/ws/orders")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Real-time update: {data}")