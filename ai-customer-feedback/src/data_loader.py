import pandas as pd
import streamlit as st

@st.cache_data
def load_csv(uploaded_file):
    return pd.read_csv(uploaded_file)
