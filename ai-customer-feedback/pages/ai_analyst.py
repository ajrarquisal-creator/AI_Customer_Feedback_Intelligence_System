from src.bootstrap import ensure_data_loaded
ensure_data_loaded()

import streamlit as st
from src.data_processor import clean_dataframe
from src.ai_service import ask_ai

st.title("AI Customer Feedback Analyst")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "df" not in st.session_state:
    st.warning("No data uploaded yet. Go to Data Management to upload a CSV.")
else:
    df = clean_dataframe(st.session_state["df"])
    question = st.text_input("Ask a question about the uploaded reviews")

    if question:
        matches = df[df["SUMMARY"].str.contains(question, case=False, na=False)]

        stats_context = (
            f"Total reviews: {len(df)}. "
            f"Average sentiment: {round(df['SENTIMENT_SCORE'].mean(), 3)}. "
            f"Products: {', '.join(df['PRODUCT'].unique())}."
        )
        sample_reviews = df[["PRODUCT", "SUMMARY", "SENTIMENT_LABEL"]].head(10).to_string(index=False)
        context = f"{stats_context}\n\nSample reviews:\n{sample_reviews}"

        with st.spinner("Thinking..."):
            answer = ask_ai(question, context)

        st.session_state["chat_history"].append({
            "question": question,
            "answer": answer,
            "matches": matches
        })

    if st.session_state["chat_history"]:
        st.markdown("### Conversation History")
        for entry in reversed(st.session_state["chat_history"]):
            st.markdown(f"**You:** {entry['question']}")
            st.markdown(f"**AI:** {entry['answer']}")
            with st.expander("Matching reviews from dataset"):
                st.dataframe(entry["matches"])
            st.divider()

        if st.button("Clear chat history"):
            st.session_state["chat_history"] = []
            st.rerun()


