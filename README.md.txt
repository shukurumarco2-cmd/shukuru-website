# RL-REIT — Week 1 Repository

## Project
**RL-REIT: A Deep Reinforcement Learning Agent for Real Estate ETF Trading**

Assigned by: Greatest Company Limited

## Week 1 scope
Week 1 covers the data foundation:
- Programmatic acquisition of VNQ, XLRE and IYR from Yahoo Finance using `yfinance`.
- Exploratory data analysis.
- Data cleaning.
- Technical feature engineering: daily return, MA_10, MA_20, MA_50, 20-day volatility, RSI_14, MACD and MACD_Signal.

The project brief specifies daily data from 1 Jan 2010 to 31 Dec 2024, with Open, High, Low, Close, Adjusted Close and Volume. Raw data must remain separate from processed data.

## Repository structure
```text
RL_REIT_Week1/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_collection.py
│   ├── data_exploration.py
│   ├── data_cleaning.py
│   └── feature_engineering.py
├── notebooks/
├── results/
│   ├── plots/
│   └── models/
├── requirements.txt
└── README.md
```

## Installation
From the repository root:

```bash
python -m pip install -r requirements.txt
```

## Run Week 1
Run these commands in order:

```bash
python src/data_collection.py
python src/data_exploration.py
python src/data_cleaning.py
python src/feature_engineering.py
```

The collection script creates `data/raw/`. Cleaning and feature engineering create files under `data/processed/`.

## Expected processed files
```text
data/processed/VNQ_clean.csv
data/processed/VNQ_features.csv
data/processed/XLRE_clean.csv
data/processed/XLRE_features.csv
data/processed/IYR_clean.csv
data/processed/IYR_features.csv
```

## Week 1 status
The four source scripts were used during the completed Week 1 workflow. The actual CSV datasets generated on the user's PC are intentionally not fabricated here; they should be copied from the user's local `rl_reit_trader/data/` folders into this repository package before submission.

## Important project rule
This is a simulated academic trading project. It is not connected to a brokerage account and must not be used to invest real money.
