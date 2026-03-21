import sys
import os


sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
import pandas as pd
from preprocessing import load_dataset, preprocess_dataset
from embeddings import embed_texts
from analysis import topic_clustering, plot_clusters, word_frequency


DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset.csv')

st.set_page_config(page_title="Corpus Linguistics Dashboard", layout="wide")
st.title("Corpus Linguistics Dashboard")

df = load_dataset(DATA_PATH)
df = preprocess_dataset(df)

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Register Distribution")
st.bar_chart(df["label"].value_counts())

st.subheader("Semantic Clustering")
embeddings = embed_texts(df['clean_text'].tolist())
labels = topic_clustering(embeddings)
fig = plot_clusters(embeddings, labels)
st.plotly_chart(fig)

st.subheader("Most Frequent Words")
freq = word_frequency(df["clean_text"])
freq_df = pd.DataFrame(freq, columns=["Word", "Count"])
st.table(freq_df)