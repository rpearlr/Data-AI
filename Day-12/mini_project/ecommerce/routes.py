from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import User, Product, Blog, Comment
from schemas import (
    UserCreate, ProductCreate, BlogCreate, CommentCreate
)

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/products")
def list_products(
    search: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Product)
    if search:
        query = query.filter(Product.name.contains(search))
    return query.all()


@router.get("/products/{product_id}")
def product_detail(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}


@router.post("/blogs")
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/blogs")
def list_blogs(db: Session = Depends(get_db)):
    return db.query(Blog).all()


@router.post("/blogs/{blog_id}/like")
def like_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).get(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.likes += 1
    db.commit()
    return {"likes": blog.likes}


@router.post("/blogs/{blog_id}/comments")
def add_comment(
    blog_id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db)
):
    new_comment = Comment(text=comment.text, blog_id=blog_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment
