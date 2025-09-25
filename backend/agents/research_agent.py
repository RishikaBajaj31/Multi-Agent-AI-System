import fitz  # PyMuPDF
from transformers import pipeline

class ResearchAgent:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self.extract_text()

    def extract_text(self):
        doc = fitz.open(self.pdf_path)
        return " ".join([page.get_text() for page in doc])

    def handle(self, query: str):
        if "summarize" in query.lower():
            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            return summarizer(self.text[:1000])[0]['summary_text']

        if "keywords" in query.lower():
            words = self.text.split()
            keywords = list(set(words))[:10]
            return f"Keywords: {keywords}"

        return "❓ I couldn't process your research query."
