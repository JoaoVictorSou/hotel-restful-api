import sqlite3
import os

DIRECTORY_PATH = os.path.abspath('.')
CONNECT_STRING = os.path.join(
    DIRECTORY_PATH,
    'data',
    'hotel.db'
)

hotels = [
    {
    'hotel_id': 'alpha',
    'name': 'Alpha Hotel',
    'star': 4.3,
    'price': 420.34,
    'city': 'Rio de Janeiro',
    },
    {
    'hotel_id': 'bravo',
    'name': 'Bravo Hotel',
    'star': 4.4,
    'price': 3800.90,
    'city': 'Santa Catarina',
    },
    {
    'hotel_id': 'charlie',
    'name': 'Charlie Hotel',
    'star': 3.9,
    'price': 320.2,
    'city': 'Santa Catarina',
    },
]
hotels = [tuple(hotel.values()) for hotel in hotels]

def create_hotel_table():
    try:
        connection = sqlite3.connect(CONNECT_STRING)
        cursor = connection.cursor()

        sql_create_hotel_table = """
            CREATE TABLE IF NOT EXISTS hotels (
                hotel_id text PRIMARY KEY,
                name text,
                star real,
                price real,
                city text
            )
        """
        cursor.execute(sql_create_hotel_table)
        
    except Exception as err:
        print(f'ERR: {err}')

    finally:
        cursor.close()
        connection.close()

def insert_hotel(hotels: list):
    # Só vai criar a tabela no caso que ela não exista.
    create_hotel_table()

    sql_insert = """
        INSERT INTO HOTELS (
            hotel_id,
            name,
            star,
            price,
            city
        ) VALUES (
            ?,
            ?,
            ?,
            ?,
            ?
        )
    """

    try:
        connection = sqlite3.connect(CONNECT_STRING)
        cursor = connection.cursor()

        cursor.executemany(
            sql_insert,
            hotels
        )

        connection.commit()

    finally:
        cursor.close()
        connection.close()

