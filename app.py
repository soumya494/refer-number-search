from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    number = request.json.get("number")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM numbers WHERE DE_ID = ? LIMIT 1",
        (number,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return jsonify({
            "found": True
        })

    return jsonify({
        "found": False
    })


if __name__ == "__main__":
    app.run(debug=True)