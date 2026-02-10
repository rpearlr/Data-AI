from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends
app = FastAPI()

books = ["Great Gatsby","Dracula"]
@app.get("/users")
def get_users():
    return books