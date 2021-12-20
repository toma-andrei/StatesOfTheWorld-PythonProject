from os import linesep
from connection import (
    get_connection_to_server,
    get_connection_to_database,
    create_database,
)

from mysql.connector import Error


connection = None


def create_db():
    global connection
    connection_to_server = get_connection_to_server("localhost", "root", "")
    query = "CREATE DATABASE states_of_the_world"
    create_database(connection_to_server, query)
    connection = get_connection_to_database(
        "localhost", "root", "", "states_of_the_world"
    )


def create_tables():
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

    cursor = connection.cursor()

    try:
        cursor.execute(drop_table)
        connection.commit()

        cursor.execute(create_stateinfo_table_query)
        connection.commit()
    except Error as e:
        print(f"Error message: '{e}'")


def populate_db():
    try:
        # create or open .txt file containing informations about countries
        file = open("clean_countries_information.txt", "r", encoding="utf8")
    except Exception as e:
        print(
            "Something went wrong opening 'clean_countries_information.txt'. Error message: "
            + str(e)
        )
    content = file.read()
    splitted = content.split("\n")
    cnt = 0

    query = "INSERT INTO stateinfo (name, capital, population, density, surface, language, timezone, regime, currency) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    lines_list = list()

    for line in splitted:
        if line:
            splitted_line = tuple(line.split("|"))
            if splitted_line not in lines_list:
                lines_list.append(splitted_line)

    cursor = connection.cursor()
    cursor.executemany(query, lines_list)
    connection.commit()


def main():
    create_db()
    create_tables()
    populate_db()


if __name__ == "__main__":
    main()
