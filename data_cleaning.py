import pandas as pd
import os

TICKERS = ["VNQ", "XLRE", "IYR"]

print("=" * 60)
print("RL-REIT DATA CLEANING")
print("=" * 60)

os.makedirs("data/processed", exist_ok=True)

for ticker in TICKERS:
    input_file = f"data/raw/{ticker}.csv"
    output_file = f"data/processed/{ticker}_clean.csv"

    print(f"\nCleaning {ticker}...")

    data = pd.read_csv(input_file)
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.sort_values("Date")
    data = data.drop_duplicates(subset="Date")

    required_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    data = data.dropna(subset=required_columns)
    data = data.reset_index(drop=True)
    data.to_csv(output_file, index=False)

    print(f"Saved: {output_file}")
    print(f"Rows after cleaning: {len(data)}")
    print(f"Missing values: {data[required_columns].isnull().sum().sum()}")

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED!")
print("=" * 60)
