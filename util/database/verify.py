import sqlite3
import os

DIRECTORY_PATH = os.path.abspath('.')
CONNECT_STRING = os.path.join(
    DIRECTORY_PATH,
    'data',
    'hotel.db'
)

def select_all_hotels():
    all_hotels = []
    
    try:
        connection = sqlite3.connect(CONNECT_STRING)
        cursor = connection.cursor()

        sql_query = """
            SELECT *
            FROM hotels
        """

        cursor.execute(sql_query)

        all_hotels = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
    
    return all_hotels

def select_all_tables_in_schema():
    all_tables = []
    
    try:
        connection = sqlite3.connect(CONNECT_STRING)
        cursor = connection.cursor()

        query = """
            SELECT name
            FROM sqlite_schema
            WHERE
                type = 'table'
                AND name NOT LIKE 'sqlite_%'
        """
        cursor.execute(query)

        all_tables = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
    
    return all_tables