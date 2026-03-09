import mysql.connector
import pandas as pd
from config.db_config import DB_CONFIG

def fetch_flights(origin, destination, flight_date):

    conn = mysql.connector.connect(**DB_CONFIG)

    query = """
        SELECT platform, airline, flight_time, price
        FROM flights
        WHERE origin=%s
        AND destination=%s
        AND flight_date=%s
    """

    df = pd.read_sql(query, conn, params=(origin, destination, flight_date))

    conn.close()
    return df