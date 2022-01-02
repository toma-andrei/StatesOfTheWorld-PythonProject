import mysql.connector
from mysql.connector import Error


def get_connection_to_server(host_name, username, password):
    """
    obtain connection to MySql database using mysql.connector
    """
    connection = None
    try:
        # get connection to database server with specific credentials
        connection = mysql.connector.connect(
            host=host_name, user=username, passwd=password
        )
    except Error as e:
        print(f"Error message: '{e}'")
    return connection


def create_database(connection, query):
    """
    Create database via query
    @param connection = connection to MySql database
    @param query = query for creating database
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except Error as e:
        print(f"Error message: '{e}'")


def get_connection_to_database(host_name, username, password, db_name):
    """
    Obtain a connection to a specific database
    @param host_name = database host name
    @param username = username for database authentication
    @param password = password for database authentication
    @param username = database for which connection is requested

    """

    connection = None
    try:
        # get connection to database with specific credentials
        connection = mysql.connector.connect(
            host=host_name, user=username, passwd=password, database=db_name
        )

    except Error as e:
        print(f"Error message: '{e}'")
    return connection
