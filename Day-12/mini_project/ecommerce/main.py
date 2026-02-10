from fastapi import FastAPI
from database import engine, Base
from routes import router

app = FastAPI(title="Ecommerce")

Base.metadata.create_all(bind=engine)

app.include_router(router)
