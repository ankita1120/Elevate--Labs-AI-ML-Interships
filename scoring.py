import spacy
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import re

# Load spaCy model (ensure installed: python -m spacy download en_core_web_sm)
try:
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    raise RuntimeError(
        "spaCy model 'en_core_web_sm' not found. Run: python -m spacy download en_core_web_sm"
    )

def preprocess_text(text):
    """Lowercase, remove non-alpha, lemmatize, remove stopwords using spaCy."""
    if not text:
        return ""
    # simple cleanup
    text = re.sub(r"\s+", " ", text)
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return " ".join(tokens)

def extract_text_from_pdf(path):
    """Extract text from PDF using PyPDF2. Returns empty string on failure."""
    try:
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            all_text = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_text.append(text)
        return " ".join(all_text)
    except Exception as e:
        # Could log here
        return ""

def extract_text(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext == ".txt":
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        except:
            return ""
    else:
        return ""

def extract_keywords_from_jd(job_desc, top_k=20):
    """Return a set of important lemmas from the job description."""
    doc = nlp(job_desc)
    # Use nouns, proper nouns, and verbs as keywords
    candidates = [token.lemma_.lower() for token in doc if token.pos_ in {"NOUN", "PROPN", "VERB"} and not token.is_stop and token.is_alpha]
    # Frequency-based selection
    freq = {}
    for c in candidates:
        freq[c] = freq.get(c, 0) + 1
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top_keywords = [w for w,_ in sorted_items[:top_k]]
    return set(top_keywords)

def rank_resumes(job_description, resume_files):
    # Preprocess job description
    jd_raw = job_description if job_description else ""
    jd_processed = preprocess_text(jd_raw)
    jd_keywords = extract_keywords_from_jd(jd_raw, top_k=30)

    # Read and preprocess resumes
    resume_texts = []
    file_names = []
    for p in resume_files:
        txt = extract_text(p)
        processed = preprocess_text(txt)
        resume_texts.append(processed)
        file_names.append(os.path.basename(p))

    # If all resume texts are empty, return zero scores
    if not any(resume_texts):
        results = [{"file": f, "score": 0.0} for f in file_names]
        return results

    # TF-IDF vectorization (include job desc)
    all_docs = [jd_processed] + resume_texts
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(all_docs)
    jd_vec = tfidf[0]
    resume_vecs = tfidf[1:]

    # Cosine similarity
    cos_scores = cosine_similarity(jd_vec, resume_vecs).flatten()

    # Keyword overlap score (normalized)
    keyword_scores = []
    for text in resume_texts:
        tokens = set(text.split())
        if not tokens:
            keyword_scores.append(0.0)
            continue
        overlap = len(jd_keywords & tokens)
        keyword_scores.append(overlap / (len(jd_keywords) if jd_keywords else 1))

    # Combine scores: give cosine more weight (e.g. 0.75 vs 0.25)
    final_scores = []
    for c, k in zip(cos_scores, keyword_scores):
        final = 0.75 * float(c) + 0.25 * float(k)
        final_scores.append(round(final, 4))

    results = []
    for fn, score in zip(file_names, final_scores):
        results.append({"file": fn, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
