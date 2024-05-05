from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/base")
def base():
    return render_template("base.html")
@app.route("/")
def root():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/services")
def services():
    return render_template("services.html")
@app.route("/careers")
def careers():
    return render_template("careers.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")
