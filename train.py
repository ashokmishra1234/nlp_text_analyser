

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# ─── Download required NLTK data ─────────────────────────────────────────────
def download_nltk_resources():
    """
    Download all NLTK resources needed for tokenization and stopwords.
    Called once when the app starts.
    """
    nltk.download("punkt",     quiet=True)
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)
    print("✅ NLTK resources ready.")


# ─── TF-IDF Vectorizer Setup ─────────────────────────────────────────────────
def get_tfidf_vectorizer() -> TfidfVectorizer:
    return TfidfVectorizer(stop_words="english", max_features=20)
