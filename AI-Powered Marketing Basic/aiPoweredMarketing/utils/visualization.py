import  matplotlib.pyplot as plt
import pandas as pd


def plot_campaign_performance (data_path, output_path="output/analytics_reports/performance.png"):
    data = pd.read_csv(data_path)
    data.plot(x="Date", y=["CTR", "Impression", "Engagements"], kind= "line", figsize=(10,6))
    plt.title("Campaign Performance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Metrics")
    plt.savefig(output_path)
    plt.close()