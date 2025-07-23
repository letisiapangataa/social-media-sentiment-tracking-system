import os
import pandas as pd
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import AZURE_ENDPOINT, AZURE_KEY

# Placeholder for Twitter/Reddit data collection
def collect_social_media_posts():
    # Replace with actual API calls to Twitter or Reddit
    return [
        {"id": 1, "text": "I love this brand!"},
        {"id": 2, "text": "This product is terrible."},
        {"id": 3, "text": "Not sure how I feel about this."}
    ]

def authenticate_client():
    credential = AzureKeyCredential(AZURE_KEY)
    client = TextAnalyticsClient(endpoint=AZURE_ENDPOINT, credential=credential)
    return client

def analyze_sentiment(client, documents):
    response = client.analyze_sentiment(documents=[d["text"] for d in documents])
    sentiments = []
    for idx, doc in enumerate(response):
        sentiments.append({
            "id": documents[idx]["id"],
            "text": documents[idx]["text"],
            "sentiment": doc.sentiment,
            "confidence_scores": doc.confidence_scores
        })
    return sentiments

def main():
    posts = collect_social_media_posts()
    client = authenticate_client()
    results = analyze_sentiment(client, posts)
    df = pd.DataFrame(results)
    df.to_csv("sentiment_results.csv", index=False)
    print("Sentiment analysis complete. Results saved to sentiment_results.csv.")

if __name__ == "__main__":
    main()
