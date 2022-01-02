from os import linesep
from connection import (
    get_connection_to_server,
    get_connection_to_database,
    create_database,
)

from mysql.connector import Error


connection = None


def create_db():
    """
    Create states_of_the_world MySql database
    """
    global connection

    # get connection to server
    connection_to_server = get_connection_to_server("localhost", "root", "")
    query = "CREATE DATABASE states_of_the_world"

    # get connection to database
    create_database(connection_to_server, query)
    connection = get_connection_to_database(
        "localhost", "root", "", "states_of_the_world"
    )


def create_tables():
    """
    Create stateinfo table
    """
    drop_table = "DROP TABLE IF EXISTS stateinfo;"

    create_stateinfo_table_query = "\
    CREATE TABLE IF NOT EXISTS stateinfo( \
    name TEXT NOT NULL,\
    capital TEXT,\
    population INT,\
    density INT,\
    surface INT,\
    language TEXT,\
    timezone TEXT,\
    regime TEXT,\
    currency TEXT);\
    "

    # get cursor to table
    cursor = connection.cursor()

    try:
        # drop table if it exists
        cursor.execute(drop_table)
        connection.commit()
        print("table dropped...")

        # create table
        cursor.execute(create_stateinfo_table_query)
        connection.commit()
        print("table created...")

    except Error as e:
        print(f"Error message: '{e}'")


def populate_db():
    """
    read clean_countries_information.txt file and write
        information to stateinfo table
    """
    try:
        # create or open .txt file containing informations about countries
        file = open("clean_countries_information.txt", "r", encoding="utf8")
    except Exception as e:
        print(
            "Something went wrong opening 'clean_countries_information.txt'.\
            Error message: " + str(e)
        )

    # read file content
    content = file.read()

    # split information by "\n" to get each line for a country
    splitted = content.split("\n")

    # query for inserting into stateinfo table
    query = "INSERT INTO stateinfo (name, capital, population, density,\
        surface, language, timezone, regime, currency) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    lines_list = list()

    # iterate throuth all country informations to create
    # touples for easy table insert
    for line in splitted:
        if line:
            # create toubles
            splitted_line = tuple(line.split("|"))

            if splitted_line not in lines_list:
                lines_list.append(splitted_line)

    # get connection to cursor
    cursor = connection.cursor()

    # insert all informations in table
    cursor.executemany(query, lines_list)

    # commit query
    connection.commit()


def main():
    """
    Execute all operation for database population
    """
    create_db()
    create_tables()
    populate_db()


if __name__ == "__main__":
    main()
