from flask import Flask, render_template, request
from password_checker import PasswordChecker
import sqlite3

app = Flask(__name__)

# helper functions:
def save_to_db(password, strength):
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("INSERT INTO history (password, strength) VALUES (?, ?)", (password, strength))
        conn.commit()
        conn.close()


def get_history():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT password, strength FROM history ORDER BY id DESC")
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/check", methods=["POST"])
def check_password():
    password = request.form["password"]

    checker = PasswordChecker(password)
    strength = checker.check_strength()
    save_to_db(password, strength)

    return render_template(
        "result.html",
        password=password,
        strength=strength
    )

@app.route("/history")
def history():
    history_data = get_history()
    return render_template("history.html", history=history_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    