import streamlit as st
import pandas as pd

def ensure_data_loaded():
    if "df" not in st.session_state:
        st.session_state["df"] = pd.read_csv("data/sample_reviews.csv")
