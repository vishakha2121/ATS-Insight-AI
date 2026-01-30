from app.ml.resume_parser import extract_text
from io import BytesIO

class DummyFile:
    def __init__(self, content, filename):
        self.file = BytesIO(content)
        self.filename = filename

def test_extract_text_txt_file():
    dummy_resume = DummyFile(
        b"Python developer with ML experience",
        "resume.txt"
    )
    text = extract_text(dummy_resume)
    assert "python" in text.lower()
