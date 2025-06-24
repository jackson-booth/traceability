from fastapi import FastAPI
from app.routes import events
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(events.router)