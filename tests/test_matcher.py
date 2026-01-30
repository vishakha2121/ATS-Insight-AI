from app.ml.matcher import match_score

def test_score():
    assert match_score("python", "python") > 50
from app.ml.matcher import match_score

def test_match_score_high_similarity():
    resume = "Python machine learning developer"
    jd = "Python ML engineer required"
    score = match_score(resume, jd)
    assert score > 50


def test_match_score_low_similarity():
    resume = "Graphic designer with Photoshop skills"
    jd = "Python ML engineer required"
    score = match_score(resume, jd)
    assert score < 50
