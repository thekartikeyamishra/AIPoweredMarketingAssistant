import pandas as pd


def analyze_campaign_performance(data_path):
    data = pd.read_csv(data_path)
    metrics = {
        "Average CTR": data["CTR"].mean(),
        "Average Impression": data["Impressions"].mean(),
        "Engagement Rate": data["Engagements"].sum() / data["Impressions"].sum(),
    }
    return metrics
