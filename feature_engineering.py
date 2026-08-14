import pandas as pd
import numpy as np
import os

TICKERS = ["VNQ", "XLRE", "IYR"]

print("=" * 60)
print("RL-REIT FEATURE ENGINEERING")
print("=" * 60)

os.makedirs("data/processed", exist_ok=True)


def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    average_gain = gain.rolling(window=period).mean()
    average_loss = loss.rolling(window=period).mean()
    rs = average_gain / average_loss
    return 100 - (100 / (1 + rs))


for ticker in TICKERS:
    input_file = f"data/processed/{ticker}_clean.csv"
    output_file = f"data/processed/{ticker}_features.csv"

    print(f"\nProcessing {ticker}...")

    data = pd.read_csv(input_file)
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.sort_values("Date")

    data["Return"] = data["Close"].pct_change()
    data["MA_10"] = data["Close"].rolling(window=10).mean()
    data["MA_20"] = data["Close"].rolling(window=20).mean()
    data["MA_50"] = data["Close"].rolling(window=50).mean()
    data["Volatility_20"] = data["Return"].rolling(window=20).std()
    data["RSI_14"] = calculate_rsi(data["Close"], period=14)

    ema_12 = data["Close"].ewm(span=12, adjust=False).mean()
    ema_26 = data["Close"].ewm(span=26, adjust=False).mean()
    data["MACD"] = ema_12 - ema_26
    data["MACD_Signal"] = data["MACD"].ewm(span=9, adjust=False).mean()

    data = data.dropna()
    data = data.reset_index(drop=True)
    data.to_csv(output_file, index=False)

    print(f"Saved: {output_file}")
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")

print("\n" + "=" * 60)
print("FEATURE ENGINEERING COMPLETED!")
print("=" * 60)
