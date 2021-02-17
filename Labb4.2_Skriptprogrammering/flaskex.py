from flask import Flask, request, render_template
import sqlite3, os
import datetime, time
from database import DataBase


app = Flask(__name__)

db = "weather.db"
d = "weather"
@app.route("/json", methods=['POST'])
def json_data():
    """Take jsondata and store it in a database"""
    req_data = request.get_json()
    sensor = req_data['sensor']
    location = req_data['location']
    temperature = req_data['temperature']
    description = req_data['description']
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d-%H:%M")

    params = (sensor, location, temperature, description, timestamp)

    if os.path.isfile(db) == False:
        DataBase.create_table(db)

    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(f"INSERT INTO weather VALUES(NULL, ?, ?, ?, ?, ?)", params)
    conn.commit()

    return "<h1>Post successfull</h1>"

@app.route("/")
def show_db():
    """Selects all from database and print it in webbrowser"""
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM weather")
    return render_template("table.html", result=c.fetchall())

if __name__ == '__main__':
    app.run()
