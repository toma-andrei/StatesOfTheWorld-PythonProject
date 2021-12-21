import json
from flask import Flask
import sys

sys.path.append("../")
from Database.connection import get_connection_to_database as db_connection
from Database.query_executor import execute_select

app = Flask(__name__)

connection = db_connection("localhost", "root", "", "states_of_the_world")


@app.route("/")
def main_page():
    return json.dumps({"working": "true"})


@app.route("/all")
def all_infos():
    global connection
    query = "SELECT * FROM stateinfo"

    data = execute_select(connection, query)

    informations = dict()

    for info in data:
        informations[info[0]] = {
            "capital": info[1],
            "population": info[2],
            "density": info[3],
            "surface": info[4],
            "language": info[5],
            "timezone": info[6],
            "regime": info[7],
            "currency": info[7],
        }
    return json.dumps(informations)


@app.route("/top-<int:number>-by-population")
def get_top_by_population(number):
    return json.dumps({"number": number})


app.run()
