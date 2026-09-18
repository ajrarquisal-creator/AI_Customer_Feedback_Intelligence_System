import streamlit as st
import pandas as pd
import os

def ensure_data_loaded():
    if "df" not in st.session_state:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, "data", "sample_reviews.csv")
        st.session_state["df"] = pd.read_csv(csv_path)
