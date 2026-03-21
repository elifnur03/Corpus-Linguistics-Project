# 📚 Corpus Linguistics Dashboard

Analyze English text using NLP and machine learning. This project classifies text by **register** (academic, spoken, news, social) using sentence embeddings, KMeans clustering, and a Streamlit web dashboard.

---

## 🗂 Project Structure

```
Corpus-Linguistics-Project/
├── data/
│   └── dataset.csv                    # Generated dataset (500 rows)
├── src/
│   ├── app.py                         # Streamlit dashboard (main entry point)
│   ├── preprocessing.py               # Text cleaning & stopword removal
│   ├── embeddings.py                  # Sentence-transformer embeddings
│   ├── analysis.py                    # KMeans clustering & word frequency
│   └── data_generator_linguistic.py   # Synthetic dataset generator
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Corpus-Linguistics-Project
   ```

2. **Create & activate a virtual environment:**

   **Windows PowerShell:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK stopwords** (first run only):
   ```bash
   python -c "import nltk; nltk.download('stopwords')"
   ```

---

## 🚀 Usage

### 📝 Generate Dataset

Run from the project root:
```bash
python src/data_generator_linguistic.py
```
Generates `data/dataset.csv` with 500 rows of English text and register labels.

### 🌐 Launch the Dashboard

```bash
streamlit run src/app.py
```

Open your browser at `http://localhost:8501` to explore:
- **Dataset Preview** — sample rows from the corpus
- **Register Distribution** — bar chart of label counts
- **Semantic Clustering** — 2D PCA scatter plot of sentence embeddings
- **Most Frequent Words** — top 10 words after preprocessing

---

## 📌 Notes

- Uses `sentence-transformers` (`all-MiniLM-L6-v2`) for semantic embeddings
- NLTK stopwords used in preprocessing
- KMeans clustering with PCA dimensionality reduction for visualization
- Interactive charts via Plotly, dashboard via Streamlit
