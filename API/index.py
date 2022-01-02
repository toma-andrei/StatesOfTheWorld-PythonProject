import sys
sys.path.append("../")
from Database.query_executor import execute_select
from Database.connection import get_connection_to_database as db_connection
from api_utils import get_json
from flask import Flask
import json


app = Flask(__name__)

connection = db_connection("localhost", "root", "", "states_of_the_world")


@app.route("/")
def main_page():
    """
    Return a json saying API is working
    """
    return json.dumps({"working": "true"})


@app.route("/all")
def all_infos():
    """
    Execute query and get all informations about a country on route "/all"
    @return json with data

    """
    global connection
    query = "SELECT * FROM stateinfo"

    data = execute_select(connection, query)

    return get_json(data)


@app.route("/top-<int:number>-by-<string:cell>")
def get_top_by_cell(number, cell):
    """
    Get top for table fields with numerical value
    @number = limit of top
    @cell = field on which top is created (population, surface, density)
    """

    global connection
    if cell in ["population", "surface", "density"]:
        query = (
            "SELECT * FROM stateinfo ORDER BY " +
            cell + " DESC LIMIT " + str(number)
        )
        data = execute_select(connection, query)
        return get_json(data)
    else:
        return json.dumps(
            {"error": "top can be made only on population, surface, density"}
        )


@app.route("/language=<string:lang>")
def get_by_language(lang):
    """
    Get all countries with a specific language
    @param lang = language on which request is made

    """
    global connection

    query = (
        "SELECT * FROM stateinfo WHERE LOWER(language) LIKE '%" +
        (lang.lower()) + "%'"
    )
    data = execute_select(connection, query)
    return get_json(data)


@app.route("/timezone=<string:timezone>")
def get_timezone(timezone):
    """
    Get all countries with a specific timezone
    @param timezone = timezone on which request is made (UTC+2, etc..)

    """
    global connection

    # get universal timezone: UTC
    constant = timezone[:3]

    # get error from UTC
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
        query = "SELECT * FROM stateinfo WHERE timezone LIKE '%" + \
            (constant) + "%'"

    data = execute_select(connection, query)

    return get_json(data)


@app.route("/regime=<string:regime>")
def get_by_regime(regime):
    """
    Get all countries with a specific political regime
    @param regime = political regime on which request is made (Unitary semi-presidential republic, etc...)
    """

    global connection

    regime = regime.replace("_", " ")

    query = "SELECT * FROM stateinfo WHERE regime LIKE '%" + regime + "%'"

    data = execute_select(connection, query)
    return get_json(data)


@app.route("/<string:country>")
def get_country(country):
    """
    Get informations about a country
    @param country = country name on which request is made

    """

    global connection

    country = country.replace("_", " ")

    query = "SELECT * FROM stateinfo WHERE LOWER(name) LIKE '%" + \
        country.lower() + "%'"

    data = execute_select(connection, query)
    return get_json(data)


app.run()
