from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")


if __name__== "__main__":
    app.run(debug=True)