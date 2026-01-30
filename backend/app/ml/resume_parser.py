from pypdf import PdfReader

def extract_text(file):
    # PDF resume handling
    if file.filename.lower().endswith(".pdf"):
        reader = PdfReader(file.file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

        return text.strip()

    # TXT resume handling
    return file.file.read().decode("utf-8", errors="ignore")
