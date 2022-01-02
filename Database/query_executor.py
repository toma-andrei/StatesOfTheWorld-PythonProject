from mysql.connector import Error


def execute_select(connection, query):
    """
    Execute a query on database and return result
    @param connection = connection to table
    @param query = query for database
    @return information fetched from database
    """

    cursor = connection.cursor()
    result = None
    try:
        # execute query
        cursor.execute(query)

        # get response from database
        result = cursor.fetchall()

        return result
    except Error as e:
        print(f"Error message: '{e}'")
