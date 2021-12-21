import json
from flask import Flask
import sys
from api_utils import get_json

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

    return get_json(data)


@app.route("/top-<int:number>-by-population")
def get_top_by_population(number):
    global connection

    query = "SELECT * FROM stateinfo ORDER BY population DESC LIMIT " + str(number)
    data = execute_select(connection, query)
    print(number)
    return get_json(data)


@app.route("/language=<string:lang>")
def get_by_language(lang):
    global connection

    query = (
        "SELECT * FROM stateinfo WHERE LOWER(language) LIKE '%" + (lang.lower()) + "%'"
    )
    data = execute_select(connection, query)
    return get_json(data)


@app.route("/timezone=<string:timezone>")
def get_timezone(timezone):
    global connection
    constant = timezone[:3]
    value = timezone[3:]
    if value:
        query = (
            "SELECT * FROM stateinfo WHERE timezone LIKE '%"
            + (constant)
            + "%' AND timezone LIKE '%"
            + (value)
            + "%'"
        )
    else:
        query = "SELECT * FROM stateinfo WHERE timezone LIKE '%" + (constant) + "%'"

    data = execute_select(connection, query)

    return get_json(data)


app.run()
