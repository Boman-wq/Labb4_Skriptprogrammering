from flask import Flask, render_template, request
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "inception"

@app.route('/')
def home():
    """Förstasidan"""
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def signup():
    """Formulär"""
    form = RegisterForm()
    if form.is_submitted():
        result = request.form
        return render_template("user.html", result=result)
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run()