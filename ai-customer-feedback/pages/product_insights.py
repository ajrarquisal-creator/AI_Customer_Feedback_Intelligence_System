from src.bootstrap import ensure_data_loaded
ensure_data_loaded()

import streamlit as st
from src.data_processor import clean_dataframe
from src.analytics import product_stats

st.title("Product Insights")

if "df" not in st.session_state:
    st.warning("No data uploaded yet. Go to Data Management to upload a CSV.")
else:
    df = clean_dataframe(st.session_state["df"])
    stats = product_stats(df)

    st.subheader("Product Comparison Table")
    st.dataframe(stats)

    selected = st.selectbox("Select a product for details", stats["PRODUCT"].tolist())
    product_df = df[df["PRODUCT"] == selected]

    st.write(f"Total reviews: {len(product_df)}")
    st.write(f"Average sentiment: {round(product_df['SENTIMENT_SCORE'].mean(), 3)}")
    st.dataframe(product_df[["DATE", "SUMMARY", "SENTIMENT_LABEL", "SENTIMENT_SCORE"]])


