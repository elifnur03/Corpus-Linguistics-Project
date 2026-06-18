from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
import plotly.express as px
from collections import Counter

def topic_clustering(embeddings, n_topics=4):
    kmeans = KMeans(n_clusters=n_topics, random_state=42)
    labels = kmeans.fit_predict(embeddings)
    return labels

def plot_clusters(embeddings, labels):
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(embeddings)

    df_plot = pd.DataFrame({
        "x": reduced[:, 0],
        "y": reduced[:, 1],
        "label": labels.astype(str)
    })

    fig = px.scatter(df_plot, x="x", y="y", color="label")
    return fig

def word_frequency(texts, top_n=10):
    words = " ".join(texts).split()
    counts = Counter(words)
    return counts.most_common(top_n)