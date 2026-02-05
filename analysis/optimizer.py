def get_best_flight(df):
    if df.empty:
        return None
    return df.loc[df["price"].idxmin()]
