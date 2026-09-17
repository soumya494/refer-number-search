from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"


# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# SEARCH MOBILE NUMBER
# =========================
@app.route("/search", methods=["POST"])
def search():

    try:
        # Get number from frontend
        data = request.get_json()

        if not data:
            return jsonify({
                "found": False,
                "status": "",
                "message": "Invalid request"
            })

        number = str(data.get("number", "")).strip()

        # Remove spaces
        number = number.replace(" ", "")

        # Validate 10 digit mobile number
        if not number.isdigit() or len(number) != 10:
            return jsonify({
                "found": False,
                "status": "",
                "message": "Please enter a valid 10-digit mobile number"
            })

        # Connect database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Search mobile number
        cursor.execute(
            '''
            SELECT "Data Status"
            FROM numbers
            WHERE Mobile = ?
            LIMIT 1
            ''',
            (number,)
        )

        result = cursor.fetchone()

        conn.close()

        # =========================
        # NUMBER FOUND
        # =========================
        if result:

            status = str(result[0]).strip()

            return jsonify({
                "found": True,
                "status": status,
                "message": "Number found"
            })

        # =========================
        # NUMBER NOT FOUND
        # =========================
        return jsonify({
            "found": False,
            "status": "",
            "message": "Number not found"
        })

    except Exception as e:

        print("Error:", e)

        return jsonify({
            "found": False,
            "status": "",
            "message": "Something went wrong"
        })


# =========================
# RUN FLASK APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)