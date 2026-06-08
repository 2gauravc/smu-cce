"""
Stock Analysis Streamlit Web App

A beginner-friendly web application for analyzing stocks by:
- Viewing financial statements (income, balance sheet, cash flow)
- Reading latest news articles
- Checking current stock price and analyst ratings

Usage:
    streamlit run app.py
"""

import streamlit as st
from helpers import (
    get_financials,
    get_news,
    get_price,
    get_analyst_ratings
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
                
                # Income Statement
                st.subheader("Income Statement")
                st.dataframe(financials['income_statement'], use_container_width=True)
                
                # Balance Sheet
                st.subheader("Balance Sheet")
                st.dataframe(financials['balance_sheet'], use_container_width=True)
                
                # Cash Flow
                st.subheader("Cash Flow Statement")
                st.dataframe(financials['cash_flow'], use_container_width=True)
            
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
            
            # Stock price and ratings analysis
            elif analysis_type == "stock price ratings":
                st.header(f"💰 Stock Price & Analyst Ratings for {ticker}")
                
                # Get price
                with st.spinner("Fetching stock price..."):
                    price = get_price(ticker)
                
                # Display price as metric
                if price:
                    st.metric(
                        label="Current Stock Price",
                        value=f"${price:.2f}"
                    )
                else:
                    st.warning("Price data not available for this ticker.")
                
                # Get analyst ratings
                st.subheader("Analyst Ratings")
                with st.spinner("Fetching analyst ratings..."):
                    ratings = get_analyst_ratings(ticker)
                
                if ratings.empty:
                    st.info("No analyst ratings found for this ticker.")
                else:
                    st.write(f"Latest {len(ratings)} analyst recommendations:")
                    st.dataframe(ratings, use_container_width=True)
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please check that the ticker symbol is valid and try again.")

# Footer with instructions
st.divider()
st.write("### How to use this app:")
st.markdown("""
1. **Enter a ticker symbol** - e.g., AAPL, GOOG, MSFT, TSLA
2. **Choose an analysis type** - Select what data you want to see
3. **Click Run Analysis** - The app will fetch and display the data
4. **Explore the results** - View financial statements, news, or stock information

**Note:** Data is fetched from Yahoo Finance in real-time.
""")
