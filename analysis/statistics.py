def price_statistics(df):
    return {
        "min_price": df["price"].min(),
        "max_price": df["price"].max(),
        "avg_price": round(df["price"].mean(), 2)
    }
