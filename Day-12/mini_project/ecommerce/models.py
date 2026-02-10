from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    blogs = relationship("Blog", back_populates="author")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(Integer)


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    likes = Column(Integer, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="blogs")

    comments = relationship("Comment", back_populates="blog")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(Text)

    blog_id = Column(Integer, ForeignKey("blogs.id"))
    blog = relationship("Blog", back_populates="comments")
