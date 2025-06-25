from fastapi import FastAPI
from app.routes import events, parts
from app.database import Base, engine
from app.exception_handlers import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI()
register_exception_handlers(app)


app.include_router(events.router)
app.include_router(parts.router)
