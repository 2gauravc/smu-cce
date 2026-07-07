"""
Helper functions for stock analysis.
Extracted from notebooks for use in the Streamlit app.
"""

import os
import re
from datetime import datetime
from pathlib import Path

try:
    import pandas as pd
except ImportError:  # pragma: no cover - handled gracefully at runtime
    pd = None

try:
    import yfinance as yf
except ImportError:  # pragma: no cover - handled gracefully at runtime
    yf = None


def _is_writable_directory(path):
    """Check whether a directory can be created and written to."""
    try:
        path.mkdir(parents=True, exist_ok=True)
        test_file = path / ".write-test"
        test_file.write_text("ok", encoding="utf-8")
        test_file.unlink(missing_ok=True)
        return True
    except OSError:
        return False


def get_analyses_dir():
    """Return the directory used for saved analyses.

    Production deployments should use the shared volume at /analyses-data when available.
    A custom path can be provided through the ANALYSES_DATA_DIR environment variable.
    If /analyses-data is not writable in a test environment, the app falls back to a
    workspace-local analyses-data directory.
    """
    configured_dir = os.getenv("ANALYSES_DATA_DIR")
    if configured_dir:
        return Path(configured_dir).expanduser()

    primary_dir = Path("/analyses-data")
    if _is_writable_directory(primary_dir):
        return primary_dir

    fallback_dir = Path(__file__).resolve().parent.parent / "analyses-data"
    if _is_writable_directory(fallback_dir):
        return fallback_dir

    return primary_dir


ANALYSES_DIR = get_analyses_dir()


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
    if yf is None:
        raise ImportError("yfinance is required to fetch stock analysis data.")

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
    if yf is None:
        raise ImportError("yfinance is required to fetch stock analysis data.")

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
    if yf is None:
        raise ImportError("yfinance is required to fetch stock analysis data.")

    try:
        stock = yf.Ticker(ticker)
        recs = stock.recommendations

        if recs is None or len(recs) == 0:
            return pd.DataFrame()

        # Return latest 10 recommendations
        return recs.tail(10)
    except Exception as e:
        raise Exception(f"Error fetching analyst ratings for {ticker}: {str(e)}")


def _sanitize_filename_part(value):
    """Convert a value into a filesystem-safe slug."""
    text = re.sub(r"[^a-z0-9]+", "-", str(value).strip().lower())
    return text.strip("-") or "analysis"


def generate_analysis_filename(ticker, analysis_type, metadata=None, timestamp=None):
    """Create an intuitive markdown filename using the ticker and selected analysis options."""
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    parts = [_sanitize_filename_part(ticker), _sanitize_filename_part(analysis_type)]

    if metadata:
        for key, value in metadata.items():
            if value not in (None, ""):
                parts.append(f"{_sanitize_filename_part(key)}-{_sanitize_filename_part(value)}")

    parts.append(timestamp)
    return "-".join(parts) + ".md"


def write_markdown_file(filename, content, output_dir=None):
    """Write markdown content to disk in the saved analyses directory."""
    destination_dir = Path(output_dir) if output_dir else ANALYSES_DIR
    destination_dir.mkdir(parents=True, exist_ok=True)

    if isinstance(filename, Path):
        target_path = filename
    elif str(filename).startswith("/"):
        target_path = Path(filename)
    else:
        target_path = destination_dir / filename

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(content, encoding="utf-8")
    return target_path


def save_analysis_as_markdown(ticker, analysis_type, markdown_content, metadata=None, output_dir=None):
    """Save a rendered analysis to markdown and return the file path."""
    filename = generate_analysis_filename(ticker, analysis_type, metadata=metadata)
    return write_markdown_file(filename, markdown_content, output_dir=output_dir)


def list_saved_analyses(output_dir=None):
    """Return all saved markdown analyses from the analyses directory."""
    destination_dir = Path(output_dir) if output_dir else ANALYSES_DIR
    if not destination_dir.exists():
        return []
    return sorted(destination_dir.glob("*.md"), key=lambda item: item.name)
