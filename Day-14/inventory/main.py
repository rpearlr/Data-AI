from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from inventory_oops import Electronics, Grocery

app = FastAPI()
templates = Jinja2Templates(directory="templates")

electronics = Electronics()
grocery = Grocery()


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "electronics": electronics.get_products(),
            "grocery": grocery.get_products()
        }
    )


@app.get("/add")
def add_page(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})


@app.post("/add")
def add_product(
    category: str = Form(...),
    name: str = Form(...),
    price: int = Form(...),
    stock: int = Form(...)
):
    product = electronics if category == "electronics" else grocery
    product.add_product(name, price, stock)
    return RedirectResponse("/", status_code=303)


@app.post("/update")
def update_stock(
    category: str = Form(...),
    name: str = Form(...),
    stock: int = Form(...)
):
    product = electronics if category == "electronics" else grocery
    product.update_stock(name, stock)
    return RedirectResponse("/", status_code=303)


@app.get("/delete/{category}/{name}")
def delete_product(category: str, name: str):
    product = electronics if category == "electronics" else grocery
    product.remove_product(name)
    return RedirectResponse("/", status_code=303)
