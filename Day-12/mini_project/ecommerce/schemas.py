from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: str
    description: str
    price: int


class ProductOut(ProductCreate):
    id: int

    class Config:
        orm_mode = True


class BlogCreate(BaseModel):
    title: str
    content: str
    user_id: int


class BlogOut(BaseModel):
    id: int
    title: str
    content: str
    likes: int

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    text: str


class CommentOut(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
