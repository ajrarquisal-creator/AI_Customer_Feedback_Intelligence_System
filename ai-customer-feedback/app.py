import streamlit as st
from src.bootstrap import ensure_data_loaded
from src.data_processor import clean_dataframe
from src.analytics import summary_stats

st.set_page_config(page_title="AI Customer Feedback Intelligence System", layout="wide")
ensure_data_loaded()

st.title("AI Customer Feedback Intelligence System")
st.write("Analyze customer reviews for outdoor, hiking, camping, and sports equipment products.")

df = clean_dataframe(st.session_state["df"])
stats = summary_stats(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Reviews", stats["total_reviews"])
col2.metric("Average Sentiment", stats["average_sentiment"])
col3.metric("Positive %", f"{stats['positive_pct']}%")
col4.metric("Negative %", f"{stats['negative_pct']}%")

st.divider()

st.subheader("Get started")
st.markdown('''
- Data Management - upload your own CSV or review the sample dataset
- Dashboard - full charts and product comparisons
- AI Analyst - ask questions about your reviews in plain English
''')

st.info("Numerical results are calculated from the dataset. AI-generated summaries are interpretations and should be reviewed by a human.")
