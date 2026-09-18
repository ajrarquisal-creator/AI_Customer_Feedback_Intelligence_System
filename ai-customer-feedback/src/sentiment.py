def classify_sentiment(score):
    if score is None:
        return "Unknown"
    try:
        score = float(score)
    except (ValueError, TypeError):
        return "Unknown"
    if score < -1 or score > 1:
        return "Unknown"
    if score <= -0.34:
        return "Negative"
    elif score < 0.34:
        return "Neutral"
    else:
        return "Positive"
