from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends
app = FastAPI()
books = ["Great Gatsby","Dracula"]
@app.get("/books")
def get_users():
    return books
@app.get("/books/{id}")
def get_user(id: int):
    if id > len(books) :
        return HTTPException
    return {"user_id": books[id]}