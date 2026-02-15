import random
import mysql.connector
from datetime import date, timedelta, time
from config.db_config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# ------------------ TABLE ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origin VARCHAR(10),
    destination VARCHAR(10),
    airline VARCHAR(50),
    platform VARCHAR(50),
    price INT,
    flight_date DATE,
    flight_time TIME
)
""")

cursor.execute("DELETE FROM flights")

# ------------------ MASTER DATA ------------------
cities = [
    "DEL","BOM","BLR","HYD","MAA","CCU","PNQ","AMD","JAI","LKO",
    "PAT","RNC","BHU","VNS","IXC","ATQ","SXR","JMU","UDR","KOTA",
    "BKN","JDH","RAJ","GWL","BPL","IDR","UJN","NAG","RPR","BBS",
    "CTC","VSKP","VGA","TIR","TRZ","MDU","CJB","IXM","KNU","AGR",
    "ALD","GOR","DBD","SRE","HRD","DDN","SHL","GAU","DIB","TEZ"
]

airlines = [
    "IndiGo","Air India","Vistara","SpiceJet","Akasa Air",
    "Go First","AirAsia India","Alliance Air","Star Air","TruJet"
]

platforms = [
    "Skyscanner","MakeMyTrip","Goibibo","Cleartrip"
]

# ------------------ DATES (NEXT 30 DAYS) ------------------
start_date = date(2026, 2, 1)
dates = [start_date + timedelta(days=i) for i in range(30)]

# ------------------ TIMES (EVERY 2 HOURS) ------------------
times = [time(h, 0) for h in range(0, 24, 2)]

# ------------------ DATA GENERATION ------------------
base_price = 2000

for origin in cities:
    for destination in cities:
        if origin == destination:
            continue

        for d in dates:
            flights_per_day = random.randint(2, 3)

            sampled_times = random.sample(times, flights_per_day)

            for t in sampled_times:
                cursor.execute("""
                INSERT INTO flights
                (origin, destination, airline, platform, price, flight_date, flight_time)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                """, (
                    origin,
                    destination,
                    random.choice(airlines),
                    random.choice(platforms),
                    base_price + random.randint(800, 7000),
                    d,
                    t
                ))

conn.commit()
cursor.close()
conn.close()

print("Large-scale realistic flight data populated.")
