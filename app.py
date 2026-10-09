from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template(
        "index.html",
        titulo="Dashboard",
        mensagem="Bem-vindo ao painel de controle."
    )


@app.route("/sobre")
def sobre():
    return render_template(
        "index.html",
        titulo="Sobre o Sistema",
        mensagem="Este sistema utiliza Python, Flask, HTML e CSS."
    )


if __name__ == "__main__":
    app.run(debug=True)
