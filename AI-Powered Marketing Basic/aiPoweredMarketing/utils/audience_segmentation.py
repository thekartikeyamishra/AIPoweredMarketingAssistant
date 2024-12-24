from sklearn.cluster import KMeans
import pandas as pd


def segment_audience(data_path, n_segments=3):
    data = pd.read_csv(data_path)
    features = data.drop(columns=["AudienceID", "Segment"])

    kmeans = KMeans(n_clusters=n_segments, random_state=42)
    data["Segment"] = kmeans.fit_predict(features)
    return data
