from transformers import pipeline

def get_sentiment(data):
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(data)