import mysql.connector
import pandas as pd
from config.db_config import DB_CONFIG

def get_flights(origin, destination):
    conn = mysql.connector.connect(**DB_CONFIG)

    query = """
        SELECT source, airline, price
        FROM flights
        WHERE origin=%s AND destination=%s
    """

    df = pd.read_sql(query, conn, params=(origin, destination))
    conn.close()
    return df
