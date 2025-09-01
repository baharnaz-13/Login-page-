from flask import Flask, render_template, request

app = Flask(__name__)

# Fake database
USER = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USER and password == PASSWORD:
            return "<h2 style='color:green; text-align:center;'>Login realizado com sucesso ✅</h2>"
        else:
            error = "Usuário ou senha inválidos ❌"
    return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)