
from flask import Flask, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)


# Tehtävä 1
@app.route('/alkuluku/<int:number>')
def alkuluku(number):

    if number < 2:
        is_prime = False
    else:
        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    return jsonify({
        "Number": number,
        "isPrime": is_prime
    })


# Tehtävä 2
@app.route('/kenttä/<icao>')
def airport(icao):

    database = Path(__file__).parent / "lentokentta.db"

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT ident, name, municipality FROM airports WHERE ident = ?",
        (icao.upper(),)
    )

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return jsonify({"error": "Airport not found"}), 404

    return jsonify({
        "ICAO": result[0],
        "Name": result[1],
        "Municipality": result[2]
    })


if __name__ == '__main__':
    app.run(port=3000)
