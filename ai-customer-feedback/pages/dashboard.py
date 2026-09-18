from src.bootstrap import ensure_data_loaded
ensure_data_loaded()

import streamlit as st
from src.data_processor import clean_dataframe
from src.analytics import summary_stats, product_stats

st.title("Dashboard")

if "df" not in st.session_state:
    st.warning("No data uploaded yet. Go to Data Management to upload a CSV.")
else:
    df = clean_dataframe(st.session_state["df"])
    stats = summary_stats(df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Reviews", stats["total_reviews"])
    col2.metric("Average Sentiment", stats["average_sentiment"])
    col3.metric("Positive %", f"{stats['positive_pct']}%")
    col4.metric("Negative %", f"{stats['negative_pct']}%")

    st.subheader("Product Comparison")
    st.dataframe(product_stats(df))


