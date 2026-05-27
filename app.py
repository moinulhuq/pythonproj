from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def user():
    # ❌ SQL Injection vulnerability
    username = request.args.get("name")
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{username}'"
    result = cursor.execute(query).fetchall()
    return {"result": str(result)}

@app.route("/secret")
def secret():
    # ❌ Exposed sensitive data
    return {"api_key": "12345-SECRET-KEY"}

@app.route("/aikido.txt")
def aikido_verify():
    return "validation.aikido.0ecb7392f12b71a20acadc7201d51694"

app.run(host="0.0.0.0", port=5050)



