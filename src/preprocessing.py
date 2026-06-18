import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def load_dataset(path):
    return pd.read_csv(path)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

def preprocess_dataset(df, text_col='text'):
    df['clean_text'] = df[text_col].apply(clean_text)
    return df