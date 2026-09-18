from src.bootstrap import ensure_data_loaded
ensure_data_loaded()

import streamlit as st
import plotly.express as px
from src.data_processor import clean_dataframe

st.title("Trends and Analytics")

if "df" not in st.session_state:
    st.warning("No data uploaded yet. Go to Data Management to upload a CSV.")
else:
    df = clean_dataframe(st.session_state["df"])
    df = df.dropna(subset=["DATE"])

    if df.empty:
        st.info("Not enough valid date information to show trends.")
    else:
        trend = df.groupby(df["DATE"].dt.to_period("D"))["SENTIMENT_SCORE"].mean().reset_index()
        trend["DATE"] = trend["DATE"].astype(str)
        fig = px.line(trend, x="DATE", y="SENTIMENT_SCORE", title="Average Sentiment Over Time")
        st.plotly_chart(fig, width='stretch')


