from flask import Flask
from flask import render_template

app = Flask("Hello World")


@app.route("/")
def hello_world():
    return render_template("index.html",name="Domink")

@app.route("/test")
def test():
    return "sorry han werk garnüt programiert lel"
if __name__ == "__main__":
    app.run(debug=True, port=5000)

