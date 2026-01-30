from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_score(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)
