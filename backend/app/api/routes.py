from fastapi import APIRouter, UploadFile, Form
from app.ml.resume_parser import extract_text
from app.ml.matcher import match_score
from app.ai.gemini_service import explain

router = APIRouter()

@router.post("/analyze")
async def analyze(resume: UploadFile, jd: str = Form(...)):
    resume_text = extract_text(resume)
    score = match_score(resume_text, jd)
    explanation = explain(score)
    return {"score": score, "explanation": explanation}
