import pandas as pd
from src.sentiment import classify_sentiment

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
    df["SENTIMENT_SCORE"] = pd.to_numeric(df["SENTIMENT_SCORE"], errors="coerce")
    df["SENTIMENT_LABEL"] = df["SENTIMENT_SCORE"].apply(classify_sentiment)
    return df
