from data_access.fetch_data import fetch_flights
from analysis.optimizer import get_best_flight
from visualization.plot_prices import plot_prices

origin = input("From city (e.g. DEL): ").upper()
destination = input("To city (e.g. BOM): ").upper()
flight_date = input("Date (YYYY-MM-DD): ")

df = fetch_flights(origin, destination, flight_date)

if df.empty:
    print("No flights found for this route/date.")
else:
    print("\nAll Flights:\n")
    print(df)

    best = get_best_flight(df)
    print("\nBest Flight:\n")
    print(best)

    plot_prices(df)
