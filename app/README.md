# Stock Analysis Web App

A beginner-friendly Streamlit web application for analyzing stocks with real-time financial data.

## Features

- 📊 **Financial Statements**: View income statements, balance sheets, and cash flow data
- 📰 **News**: Read the latest news articles about stocks
- 💰 **Stock Price & Ratings**: Check current stock prices and analyst recommendations

## Installation

1. **Navigate to the project directory:**
   ```bash
   cd smu-cce
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

From the `smu-cce` directory, run:

```bash
python -m streamlit run app/app.py
```

This will start a local web server. The app will open in your default browser at `http://localhost:8501`.

## How to Use

1. **Enter a Stock Ticker**: Type a valid stock symbol (e.g., AAPL, GOOG, MSFT, TSLA) in the sidebar
2. **Choose Analysis Type**: Select one of three analyses:
   - **filings**: View financial statements (income statement, balance sheet, cash flow)
   - **news**: Read the latest 5 news articles about the stock
   - **stock price ratings**: Check the current price and latest analyst recommendations
3. **Click "Run Analysis"**: The app will fetch and display the data
4. **Explore Results**: View the formatted data using Streamlit components

## Project Structure

```
app/
├── app.py           # Main Streamlit application
├── helpers.py       # Reusable functions for data fetching
└── README.md        # This file
```

## Code Overview

### helpers.py

Contains four main functions:

- **`get_financials(ticker)`**: Fetches financial statements (income, balance sheet, cash flow)
- **`get_news(ticker)`**: Fetches the latest 5 news articles
- **`get_price(ticker)`**: Fetches the current stock price
- **`get_analyst_ratings(ticker)`**: Fetches analyst recommendations

Each function includes:
- Type hints and docstrings for clarity
- Error handling with descriptive messages
- Data validation

### app.py

Main Streamlit application with:
- Clean UI with sidebar for inputs
- Three analysis modes corresponding to the helper functions
- Professional formatting using Streamlit components:
  - `st.write()`: Display text and data
  - `st.dataframe()`: Display tables
  - `st.metric()`: Display key metrics
- Comprehensive error handling
- Instructional footer

## Data Source

All data is fetched from **Yahoo Finance** using the `yfinance` library.

## Requirements

- Python 3.8+
- streamlit>=1.28.0
- yfinance>=0.2.0
- pandas>=1.5.0

## Learning Notes

This is a great project for students to learn:
- **Web UI Development**: Building interactive web apps with Streamlit
- **API Integration**: Fetching data from financial APIs
- **Data Handling**: Working with pandas DataFrames
- **Function Decomposition**: Breaking down notebooks into reusable functions
- **Error Handling**: Implementing try-except blocks for robustness
- **Code Documentation**: Writing docstrings and comments

## Troubleshooting

**Issue**: "No module named 'streamlit'"
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: "No analyst ratings found"
- **Solution**: Not all stocks have analyst coverage. Try large-cap stocks like AAPL, MSFT, GOOG

**Issue**: "Error fetching data"
- **Solution**: Verify the ticker symbol is correct and that you have an internet connection

## Future Enhancements

Students could extend this app with:
- Historical price charts using `plotly` or `matplotlib`
- Technical indicators (moving averages, RSI, etc.)
- Portfolio tracking across multiple stocks
- Stock comparison features
- Price prediction using machine learning
