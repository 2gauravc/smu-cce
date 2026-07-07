"""
Stock Analysis Streamlit Web App

A beginner-friendly web application for analyzing stocks by:
- Viewing financial statements (income, balance sheet, cash flow)
- Reading latest news articles
- Checking current stock price and analyst ratings

Usage:
    streamlit run app.py
"""

from urllib.parse import quote

import streamlit as st

from helpers import (
    ANALYSES_DIR,
    get_analyst_ratings,
    get_financials,
    get_news,
    get_price,
    list_saved_analyses,
    save_analysis_as_markdown,
)

# Page configuration
st.set_page_config(
    page_title="Stock Analysis App",
    page_icon="📈",
    layout="wide"
)

# Title and description
st.title("📈 Stock Analysis App")
st.write("Analyze stocks with real-time financial data, news, and analyst ratings.")

if "analysis_markdown" not in st.session_state:
    st.session_state.analysis_markdown = None
if "analysis_ticker" not in st.session_state:
    st.session_state.analysis_ticker = ""
if "analysis_type" not in st.session_state:
    st.session_state.analysis_type = "filings"
if "last_saved_path" not in st.session_state:
    st.session_state.last_saved_path = None

# Sidebar for input
st.sidebar.header("Analysis Parameters")

# Text input for ticker symbol
ticker = st.sidebar.text_input(
    "Enter Stock Ticker Symbol",
    value="AAPL",
    help="e.g., AAPL, GOOG, MSFT, TSLA"
).upper()

# Dropdown for analysis type
analysis_type = st.sidebar.selectbox(
    "Choose Analysis Type",
    options=["filings", "news", "stock price ratings"],
    help="Select what analysis you want to perform"
)

analysis_markdown = None

# Run button
if st.sidebar.button("🚀 Run Analysis", use_container_width=True):
    if not ticker:
        st.error("❌ Please enter a ticker symbol")
    else:
        try:
            # Filings analysis
            if analysis_type == "filings":
                st.header(f"📊 Financial Statements for {ticker}")

                with st.spinner("Fetching financial data..."):
                    financials = get_financials(ticker)

                st.subheader("Income Statement")
                st.dataframe(financials['income_statement'], use_container_width=True)

                st.subheader("Balance Sheet")
                st.dataframe(financials['balance_sheet'], use_container_width=True)

                st.subheader("Cash Flow Statement")
                st.dataframe(financials['cash_flow'], use_container_width=True)

                analysis_markdown = (
                    f"# Financial Statements for {ticker}\n\n"
                    f"**Analysis Type:** {analysis_type}\n\n"
                    "## Income Statement\n\n"
                    f"```text\n{financials['income_statement'].to_string()}\n```\n\n"
                    "## Balance Sheet\n\n"
                    f"```text\n{financials['balance_sheet'].to_string()}\n```\n\n"
                    "## Cash Flow Statement\n\n"
                    f"```text\n{financials['cash_flow'].to_string()}\n```"
                )
                st.session_state.analysis_markdown = analysis_markdown
                st.session_state.analysis_ticker = ticker
                st.session_state.analysis_type = analysis_type

            # News analysis
            elif analysis_type == "news":
                st.header(f"📰 Latest News for {ticker}")

                with st.spinner("Fetching news articles..."):
                    articles = get_news(ticker)

                if not articles:
                    st.info("No news articles found for this ticker.")
                else:
                    st.write(f"Found {len(articles)} recent articles:")

                    for i, article in enumerate(articles, 1):
                        with st.container(border=True):
                            st.write(f"**{i}. {article['title']}**")
                            st.write(f"📝 {article['description'][:300]}...")

                article_lines = [
                    f"- {article['title']}: {article['description']}"
                    for article in articles
                ]
                analysis_markdown = (
                    f"# Latest News for {ticker}\n\n"
                    f"**Analysis Type:** {analysis_type}\n\n"
                    f"{'\n'.join(article_lines) if article_lines else 'No news articles found.'}"
                )
                st.session_state.analysis_markdown = analysis_markdown
                st.session_state.analysis_ticker = ticker
                st.session_state.analysis_type = analysis_type

            # Stock price and ratings analysis
            elif analysis_type == "stock price ratings":
                st.header(f"💰 Stock Price & Analyst Ratings for {ticker}")

                with st.spinner("Fetching stock price..."):
                    price = get_price(ticker)

                if price:
                    st.metric(
                        label="Current Stock Price",
                        value=f"${price:.2f}"
                    )
                    price_text = f"${price:.2f}"
                else:
                    st.warning("Price data not available for this ticker.")
                    price_text = "N/A"

                st.subheader("Analyst Ratings")
                with st.spinner("Fetching analyst ratings..."):
                    ratings = get_analyst_ratings(ticker)

                if ratings.empty:
                    st.info("No analyst ratings found for this ticker.")
                    ratings_text = "No analyst ratings found."
                else:
                    st.write(f"Latest {len(ratings)} analyst recommendations:")
                    st.dataframe(ratings, use_container_width=True)
                    ratings_text = ratings.to_string()

                analysis_markdown = (
                    f"# Stock Price and Analyst Ratings for {ticker}\n\n"
                    f"**Analysis Type:** {analysis_type}\n\n"
                    f"**Current Price:** {price_text}\n\n"
                    "## Analyst Ratings\n\n"
                    f"```text\n{ratings_text}\n```"
                )
                st.session_state.analysis_markdown = analysis_markdown
                st.session_state.analysis_ticker = ticker
                st.session_state.analysis_type = analysis_type

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please check that the ticker symbol is valid and try again.")

analysis_markdown = st.session_state.get("analysis_markdown")
if analysis_markdown:
    st.divider()
    st.caption(f"Saving to: {ANALYSES_DIR}")
    if st.button("💾 Save this analysis", use_container_width=True):
        saved_path = save_analysis_as_markdown(
            ticker=st.session_state.get("analysis_ticker", ticker),
            analysis_type=st.session_state.get("analysis_type", analysis_type),
            markdown_content=analysis_markdown,
        )
        st.session_state.last_saved_path = saved_path
        st.success(f"Saved analysis to {saved_path.name}")
        st.rerun()

if st.session_state.get("last_saved_path"):
    st.info(f"Last saved file: {st.session_state.last_saved_path.name}")

st.divider()
st.subheader("📁 Saved Analyses")
saved_files = list_saved_analyses()

if not saved_files:
    st.info("No saved analyses yet. Run an analysis and save it to create a markdown report.")
else:
    for saved_file in saved_files:
        markdown_content = saved_file.read_text(encoding="utf-8")
        encoded_content = quote(markdown_content)
        data_url = f"data:text/markdown;charset=utf-8,{encoded_content}"
        st.markdown(
            f'<a href="{data_url}" target="_blank" rel="noopener noreferrer">{saved_file.name}</a>',
            unsafe_allow_html=True,
        )

# Footer with instructions
st.divider()
st.write("### How to use this app:")
st.markdown("""
1. **Enter a ticker symbol** - e.g., AAPL, GOOG, MSFT, TSLA
2. **Choose an analysis type** - Select what data you want to see
3. **Click Run Analysis** - The app will fetch and display the data
4. **Save useful reports** - Keep markdown copies of analyses for later review

**Note:** Data is fetched from Yahoo Finance in real-time.
""")
