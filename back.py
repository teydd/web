from flask import Flask,render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def product():
    return render_template("products.html")

@app.route("/contact")
def contacts():
    return render_template("contact.html")

@app.route("/about")
def abouts():
    return render_template("about.html")


if __name__=="__main__":
    app.run("0.0.0.0",443,True)