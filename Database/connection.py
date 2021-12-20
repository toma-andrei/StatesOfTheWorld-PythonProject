import mysql.connector
from mysql.connector import Error


def get_connection_to_server(host_name, username, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=username, passwd=password
        )
    except Error as e:
        print(f"Error message: '{e}'")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except Error as e:
        print(f"Error message: '{e}'")


def get_connection_to_database(host_name, username, password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=username, passwd=password, database=db_name
        )

    except Error as e:
        print(f"Error message: '{e}'")
    return connection
