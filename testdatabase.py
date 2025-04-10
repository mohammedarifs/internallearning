import pandas as pd
import mysql.connector
from mysql.connector import Error

def read_table_from_mysql(host, user, password, database, table_name):
    connection = None  # Initialize connection to None
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            database=database
        )

        if connection.is_connected():
            # Use pandas to read SQL table into a DataFrame
            query = f"SELECT * FROM {table_name};"
            df = pd.read_sql(query, connection)

            print(f"Data from {table_name} table:")
            print(df)

            return df
        else:
            print("Failed to connect to the database.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Example usage
host = 'localhost'
user = 'mohshaik13'
password = 'Arif@Mar25'
database = 'projects'
table_name = 'Tb_sample'

df = read_table_from_mysql(host, user, password, database, table_name)
