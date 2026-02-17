import os
from flask import Flask, render_template, request, redirect, url_for, session


from extensions import db
from models import User


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()

    return render_template("login.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
