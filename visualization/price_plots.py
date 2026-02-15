import matplotlib
matplotlib.rcParams['toolbar'] = 'None'

import matplotlib.pyplot as plt

def plot_prices(df):
    df = df.sort_values("price").reset_index(drop=True)

    plt.figure(figsize=(10,5))
    plt.plot(df.index, df["price"], marker="o")

    plt.xticks(df.index, df["platform"], rotation=30)
    plt.xlabel("Platform")
    plt.ylabel("Price")
    plt.title("Flight Price Comparison")

    plt.grid(True)
    plt.gca().set_navigate(False)
    plt.tight_layout()
    plt.show()
