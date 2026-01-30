from fastapi.testclient import TestClient
from app.main import app
from io import BytesIO

client = TestClient(app)

def test_analyze_api():
    resume_content = b"Python developer with machine learning experience"
    files = {
        "resume": ("resume.txt", BytesIO(resume_content), "text/plain")
    }
    data = {
        "jd": "Looking for Python ML engineer"
    }

    response = client.post("/analyze", files=files, data=data)

    assert response.status_code == 200
    json_data = response.json()
    assert "score" in json_data
    assert "explanation" in json_data
