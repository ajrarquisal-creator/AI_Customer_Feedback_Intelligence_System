import pandas as pd

REQUIRED_COLUMNS = ["PRODUCT", "DATE", "SUMMARY", "SENTIMENT_SCORE"]

def validate_columns(df: pd.DataFrame):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        return False, f"Missing required columns: {', '.join(missing)}"
    return True, "All required columns are available."

def validate_not_empty(df: pd.DataFrame):
    if df is None or df.empty:
        return False, "The uploaded file is empty."
    return True, "File contains data."

def count_missing_summaries(df: pd.DataFrame):
    return int(df["SUMMARY"].isna().sum()) if "SUMMARY" in df.columns else 0

def count_invalid_sentiment_scores(df: pd.DataFrame):
    if "SENTIMENT_SCORE" not in df.columns:
        return 0
    numeric = pd.to_numeric(df["SENTIMENT_SCORE"], errors="coerce")
    invalid = numeric.isna() | (numeric < -1) | (numeric > 1)
    return int(invalid.sum())

def count_invalid_dates(df: pd.DataFrame):
    if "DATE" not in df.columns:
        return 0
    parsed = pd.to_datetime(df["DATE"], errors="coerce")
    return int(parsed.isna().sum())
