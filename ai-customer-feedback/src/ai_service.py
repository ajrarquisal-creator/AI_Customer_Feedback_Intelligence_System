import streamlit as st
from openai import OpenAI

def get_client():
    api_key = st.secrets.get("GROQ_API_KEY", "")
    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

def ask_ai(question: str, context: str) -> str:
    client = get_client()
    system_prompt = (
        "You are an assistant analyzing customer feedback. "
        "Use only the review data and calculated statistics provided in the context. "
        "Do not invent products, reviews, statistics, customer opinions, or causes. "
        "If the information is not available, clearly say the dataset does not provide enough evidence. "
        "Separate confirmed numerical facts from interpretation."
    )
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
            ],
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI request failed: {e}"
