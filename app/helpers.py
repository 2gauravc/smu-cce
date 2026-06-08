"""
Helper functions for stock analysis.
Extracted from notebooks for use in the Streamlit app.
"""

import yfinance as yf
import pandas as pd


def get_financials(ticker):
    """
    Fetch financial statements for a given ticker symbol.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'GOOG')
    
    Returns:
        dict: Dictionary containing income statement, balance sheet, and cash flow
    """
    try:
        stock = yf.Ticker(ticker)
        
        results = {
            'income_statement': stock.financials.head(),
            'balance_sheet': stock.balance_sheet.head(),
            'cash_flow': stock.cashflow.head()
        }
        
        return results
    except Exception as e:
        raise Exception(f"Error fetching financials for {ticker}: {str(e)}")


def get_news(ticker):
    """
    Fetch the latest news articles for a given ticker symbol.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'GOOG')
    
    Returns:
        list: List of news articles with title and description
    """
    try:
        stock = yf.Ticker(ticker)
        news = stock.news
        
        if not news:
            return []
        
        articles = []
        for article in news[:5]:  # Get top 5 articles
            content = article.get("content", {})
            articles.append({
                'title': content.get("title", "No title"),
                'description': content.get("description", "No description")
            })
        
        return articles
    except Exception as e:
        raise Exception(f"Error fetching news for {ticker}: {str(e)}")


def get_price(ticker):
    """
    Fetch the current stock price for a given ticker symbol.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'GOOG')
    
    Returns:
        float: Current stock price, or None if not available
    """
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get("currentPrice")
        return price
    except Exception as e:
        raise Exception(f"Error fetching price for {ticker}: {str(e)}")


def get_analyst_ratings(ticker):
    """
    Fetch analyst ratings and recommendations for a given ticker symbol.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL', 'GOOG')
    
    Returns:
        pd.DataFrame: DataFrame of analyst recommendations, or empty DataFrame if none available
    """
    try:
        stock = yf.Ticker(ticker)
        recs = stock.recommendations
        
        if recs is None or len(recs) == 0:
            return pd.DataFrame()
        
        # Return latest 10 recommendations
        return recs.tail(10)
    except Exception as e:
        raise Exception(f"Error fetching analyst ratings for {ticker}: {str(e)}")
