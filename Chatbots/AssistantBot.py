import streamlit as st
import speech_recognition as sr
import pyttsx3
import os
from groq import Groq
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas

# ------------------ CONFIG ------------------ #

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"

client = Groq(api_key=API_KEY)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

# ------------------ FUNCTIONS ------------------ #

# Text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech to text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return "Sorry, could not understand"

# Groq response
def get_response(prompt):
    try:
        res = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1024
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Extract PDF text
def extract_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Summarize PDF
def summarize_pdf(text):
    prompt = f"Summarize this document clearly:\n\n{text[:4000]}"
    return get_response(prompt)

# Create downloadable PDF
def create_pdf(text, filename="summary.pdf"):
    c = canvas.Canvas(filename)
    y = 800

    for line in text.split("\n"):
        c.drawString(40, y, line[:90])
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    c.save()
    return filename

# ------------------ UI ------------------ #

st.set_page_config(page_title="AI Voice Assistant", layout="wide")

st.title("🤖 Voice Assistant + PDF Summarizer")

# Session state
if "chat" not in st.session_state:
    st.session_state.chat = []

# ------------------ INPUT SECTION ------------------ #

col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input("💬 Ask something")

with col2:
    if st.button("🎤 Speak"):
        user_input = listen()
        st.write("You said:", user_input)

# Send button
if st.button("Send"):
    if user_input:
        response = get_response(user_input)

        st.session_state.chat.append({
            "question": user_input,
            "answer": response,
            "feedback": None
        })

        speak(response)

# ------------------ CHAT DISPLAY ------------------ #

st.subheader("💬 Chat History")

for i, msg in enumerate(st.session_state.chat):
    st.markdown(f"**🧑 You:** {msg['question']}")
    st.markdown(f"**🤖 Bot:** {msg['answer']}")

    col1, col2 = st.columns(2)

    # 👍 LIKE
    if col1.button("👍 Like", key=f"like_{i}"):
        st.session_state.chat[i]["feedback"] = "like"
        st.success("Feedback recorded ✅")

    # 👎 DISLIKE
    if col2.button("👎 Dislike", key=f"dislike_{i}"):
        st.session_state.chat[i]["feedback"] = "dislike"

        improved = get_response(
            f"Improve and correct this answer:\n{msg['answer']}"
        )

        st.session_state.chat[i]["answer"] = improved
        st.warning("Improved response generated 🔄")

# ------------------ PDF SECTION ------------------ #

st.subheader("📄 Upload PDF")

file = st.file_uploader("Upload PDF", type=["pdf"])

if file:
    st.info("Processing...")

    text = extract_pdf(file)

    if not text.strip():
        st.error("Could not read PDF (maybe scanned file)")
    else:
        summary = summarize_pdf(text)

        st.markdown("### 📌 Summary:")
        st.write(summary)

        pdf_file = create_pdf(summary)

        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📥 Download Summary PDF",
                data=f,
                file_name="summary.pdf",
                mime="application/pdf"
            )