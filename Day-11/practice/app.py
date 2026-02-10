from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route("/")
def home() :
    return "Hello Flask"

@app.route("/about")
def about() :
    return "About page"

@app.route("/user/<name>") 
def user(name) :
    return f"Hello {name}"

@app.route("/hello")
def hello() :
    return render_template("index.html")

@app.route("/form")
def form() :
    return render_template("form.html")

@app.route("/submit",methods=["POST"])
def submit() :
    username = request.form["username"]
    return f"Hello {username}"

UPLOAD_FOLDER = r"C:\Users\User\Desktop\CapG-LS\Day-11\practice\static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/file")
def file():
    return render_template("file.html")

@app.route("/image", methods=["POST"])
def image():
    file = request.files["file"]  

    if file.filename == "":
        return "No file selected"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)
    print(filepath)
    return render_template("show.html", filename=rf"{file.filename}")


if __name__=="__main__" :
    app.run(debug=True)