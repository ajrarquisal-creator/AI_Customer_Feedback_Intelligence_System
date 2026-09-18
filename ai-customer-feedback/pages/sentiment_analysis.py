from src.bootstrap import ensure_data_loaded
ensure_data_loaded()

import streamlit as st
import plotly.express as px
from src.data_processor import clean_dataframe

st.title("Sentiment Analysis")

if "df" not in st.session_state:
    st.warning("No data uploaded yet. Go to Data Management to upload a CSV.")
else:
    df = clean_dataframe(st.session_state["df"])

    fig = px.histogram(df, x="SENTIMENT_LABEL", color="SENTIMENT_LABEL", title="Sentiment Distribution")
    st.plotly_chart(fig, width='stretch')

    st.subheader("Most Positive Reviews")
    st.dataframe(df.sort_values("SENTIMENT_SCORE", ascending=False).head(5))

    st.subheader("Most Negative Reviews")
    st.dataframe(df.sort_values("SENTIMENT_SCORE", ascending=True).head(5))


