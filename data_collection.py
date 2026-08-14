import os
import yfinance as yf

TICKERS = ["VNQ", "XLRE", "IYR"]
START_DATE = "2010-01-01"
END_DATE = "2025-01-01"

os.makedirs("data/raw", exist_ok=True)

print("Starting data collection...")
print(f"Date range: {START_DATE} to 2024-12-31")
print()

for ticker in TICKERS:
    print(f"Downloading {ticker}...")

    data = yf.download(
        ticker,
        start=START_DATE,
        end=END_DATE,
        auto_adjust=False,
        progress=False,
    )

    if data.empty:
        print(f"ERROR: No data found for {ticker}")
        continue

    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    required_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    available_columns = [c for c in required_columns if c in data.columns]
    data = data[available_columns]

    output_file = f"data/raw/{ticker}.csv"
    data.to_csv(output_file)

    print(f"Saved: {output_file}")
    print(f"Rows: {len(data)}")
    print()

print("DATA COLLECTION COMPLETED!")
