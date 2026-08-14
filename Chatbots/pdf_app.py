import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas

# ---------------- INIT ---------------- #

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama-3.1-8b-instant"

client = Groq(api_key=API_KEY)

# ---------------- FUNCTIONS ---------------- #

#  Extract text from PDF
def extract_text(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


#  Summarize using Groq
def summarize_text(text):
    prompt = f"""
    Summarize the following PDF content clearly.
    Use bullet points and keep it concise:

    {text[:4000]}
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=800
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


#  Generate PDF
def create_summary_pdf(summary, filename="summary.pdf"):
    c = canvas.Canvas(filename)
    y = 800

    for line in summary.split("\n"):
        c.drawString(40, y, line[:90])
        y -= 20

        if y < 40:
            c.showPage()
            y = 800

    c.save()
    return filename


# ---------------- UI ---------------- #

st.set_page_config(page_title="PDF Summarizer", layout="centered")

st.title(" AI PDF Summarizer (Groq)")
st.write("Upload a PDF and get a summarized version")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.info("Processing PDF...")

    # Step 1: Extract text
    pdf_text = extract_text(uploaded_file)

    if not pdf_text.strip():
        st.error(" Could not extract text (maybe scanned PDF)")
    else:
        # Step 2: Summarize
        summary = summarize_text(pdf_text)

        st.subheader(" Summary")
        st.write(summary)

        # Step 3: Create PDF
        pdf_file = create_summary_pdf(summary)

        # Step 4: Download
        with open(pdf_file, "rb") as f:
            st.download_button(
                label=" Download Summary PDF",
                data=f,
                file_name="summary.pdf",
                mime="application/pdf"
            )