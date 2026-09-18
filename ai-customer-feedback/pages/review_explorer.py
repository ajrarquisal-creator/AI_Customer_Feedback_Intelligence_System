from src.bootstrap import ensure_data_loaded
ensure_data_loaded()

import streamlit as st
from src.data_processor import clean_dataframe

st.title("Review Explorer")

if "df" not in st.session_state:
    st.warning("No data uploaded yet. Go to Data Management to upload a CSV.")
else:
    df = clean_dataframe(st.session_state["df"])

    search_text = st.text_input("Search review text")
    product_filter = st.selectbox("Filter by product", ["All"] + sorted(df["PRODUCT"].dropna().unique().tolist()))
    sentiment_filter = st.selectbox("Filter by sentiment", ["All", "Positive", "Neutral", "Negative"])

    filtered = df.copy()
    if search_text:
        filtered = filtered[filtered["SUMMARY"].str.contains(search_text, case=False, na=False)]
    if product_filter != "All":
        filtered = filtered[filtered["PRODUCT"] == product_filter]
    if sentiment_filter != "All":
        filtered = filtered[filtered["SENTIMENT_LABEL"] == sentiment_filter]

    st.write(f"Showing {len(filtered)} reviews")
    st.dataframe(filtered)

    st.download_button(
        "Download filtered reviews as CSV",
        filtered.to_csv(index=False),
        file_name="filtered_reviews.csv"
    )


