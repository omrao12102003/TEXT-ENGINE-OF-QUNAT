Text-Driven Quant Risk Intelligence System

Overview

This project is a text-driven quantitative risk engine that converts natural language portfolio requests into structured financial risk analytics and regulatory validation outputs.

Users describe portfolios in plain text. The system processes the request through multiple quantitative phases and produces risk metrics such as Value at Risk (VaR), Expected Shortfall (ES), and Basel-style backtesting validation.

System Architecture

Natural Language Input
→ Phase 1: Intent Parsing
→ Phase 2: Market Data & Portfolio Construction
→ Phase 3: Risk Modeling
→ Phase 4: Basel Backtesting

Phases

Phase 1 – Intent Parsing
Extracts assets, weights, and date range from text input using structured validation.

Phase 2 – Market Data Engine
Maps assets to tickers, fetches market data, computes log returns and covariance matrix, and builds portfolio return series.

Phase 3 – Risk Modeling
Implements:

Historical VaR

Variance-Covariance VaR

Monte Carlo VaR

Expected Shortfall

Phase 4 – Model Validation
Implements:

VaR breach detection

Kupiec Unconditional Coverage test

Basel Traffic Light classification

Example Input

NIFTY50 (50%) SP500 (50%) daily 2024

Example Output

Portfolio statistics

Covariance matrix

99% 10-day VaR

Expected Shortfall

Backtesting results

Basel classification

Technology Stack

Python 3.10+
NumPy
Pandas
SciPy
Pydantic
yfinance

How to Run

Create virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

python -m pip install -r requirements.txt

Run:

python main.py

Project Objective

This system demonstrates quantitative finance engineering, risk modeling, and statistical validation through a structured multi-phase architecture.
