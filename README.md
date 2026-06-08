# SMU CCE Financial Data Notebooks

A collection of Jupyter notebooks for fetching and analyzing financial data using yfinance.

## Notebooks

1. **filings.ipynb** - SEC Financial Statements
   - Retrieves income statement, balance sheet, and cash flow data for any stock ticker

2. **news.ipynb** - Stock News
   - Fetches and displays the latest news articles for a given stock

3. **stock_price_ratings.ipynb** - Stock Price & Analyst Ratings
   - Gets current stock price and analyst recommendations/ratings

## Setup

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab

### Installation

1. Clone or navigate to this repository:
```bash
cd smu-cce
```

2. Create a virtual environment (optional but recommended):
```bash
cd ../ 
python -m venv cce-env
source cce-env/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Notebooks

### Option 1: Using Jupyter Notebook
```bash
cd smu-cce/
jupyter notebook notebooks/
```
Then open the desired `.ipynb` file in your browser and run the cells.

### Option 2: Using JupyterLab
```bash
jupyter lab notebooks/
```

### Option 3: Using VS Code
1. Install the Jupyter extension in VS Code
2. Open any `.ipynb` file
3. Run cells individually or use "Run All"

## Example Usage

Each notebook contains example function calls. For instance, to get financials for Micron (MU):

```python
get_financials("MU")
```

To get news for Google (GOOG):

```python
get_news("GOOG")
```

To get price and ratings for a stock:

```python
get_price("AAPL")
get_analyst_ratings("AAPL")
```

## Notes

- Stock tickers should be valid symbols (e.g., AAPL, GOOGL, MSFT, etc.)
- Data is sourced from Yahoo Finance via the yfinance library
- Some stocks may not have analyst ratings available
