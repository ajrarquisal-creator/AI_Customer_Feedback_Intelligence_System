import pandas as pd

def summary_stats(df: pd.DataFrame) -> dict:
    total = len(df)
    avg = round(df["SENTIMENT_SCORE"].mean(), 3) if total else 0
    pos = int((df["SENTIMENT_LABEL"] == "Positive").sum())
    neu = int((df["SENTIMENT_LABEL"] == "Neutral").sum())
    neg = int((df["SENTIMENT_LABEL"] == "Negative").sum())
    return {
        "total_reviews": total,
        "average_sentiment": avg,
        "positive_count": pos,
        "neutral_count": neu,
        "negative_count": neg,
        "positive_pct": round(100 * pos / total, 1) if total else 0,
        "neutral_pct": round(100 * neu / total, 1) if total else 0,
        "negative_pct": round(100 * neg / total, 1) if total else 0,
    }

def product_stats(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("PRODUCT").agg(
        total_reviews=("SENTIMENT_SCORE", "count"),
        average_sentiment=("SENTIMENT_SCORE", "mean"),
    ).reset_index().sort_values("average_sentiment", ascending=False)
