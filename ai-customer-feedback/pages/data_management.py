from src.bootstrap import ensure_data_loaded
ensure_data_loaded()

import streamlit as st
from src.data_loader import load_csv
from src.data_validator import (
    validate_columns, validate_not_empty,
    count_missing_summaries, count_invalid_sentiment_scores, count_invalid_dates
)

st.title("Data Management")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = load_csv(uploaded_file)

    ok_empty, msg_empty = validate_not_empty(df)
    if not ok_empty:
        st.error(msg_empty)
    else:
        ok_cols, msg_cols = validate_columns(df)
        if not ok_cols:
            st.error(msg_cols)
        else:
            st.success("Data uploaded successfully.")
            st.success(msg_cols)
            st.info(f"There are {count_missing_summaries(df)} missing review summaries.")
            st.info(f"There are {count_invalid_sentiment_scores(df)} invalid sentiment scores.")
            st.info(f"The DATE column contains {count_invalid_dates(df)} invalid dates.")

            st.session_state["df"] = df
            st.subheader("Preview")
            st.dataframe(df.head())
else:
    st.info("Please upload a CSV file to begin.")


