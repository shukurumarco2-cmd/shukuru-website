import pandas as pd

TICKERS = ["VNQ", "XLRE", "IYR"]

print("=" * 60)
print("RL-REIT DATA EXPLORATION")
print("=" * 60)

for ticker in TICKERS:
    file_path = f"data/raw/{ticker}.csv"

    print(f"\n{'-' * 60}")
    print(f"EXPLORING: {ticker}")
    print(f"{'-' * 60}")

    data = pd.read_csv(file_path, index_col=0)
    data.index = pd.to_datetime(data.index)

    print("\nFirst 5 rows:")
    print(data.head())

    print("\nLast 5 rows:")
    print(data.tail())

    print("\nDataset shape:")
    print(data.shape)

    print("\nColumns:")
    print(list(data.columns))

    print("\nDate range:")
    print("Start:", data.index.min())
    print("End:", data.index.max())

    print("\nMissing values:")
    print(data.isnull().sum())

    print("\nData types:")
    print(data.dtypes)

    print("\nSummary statistics:")
    print(data.describe())

print("\n" + "=" * 60)
print("DATA EXPLORATION COMPLETED!")
print("=" * 60)
