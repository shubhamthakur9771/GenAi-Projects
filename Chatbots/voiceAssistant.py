import streamlit as st
import speech_recognition as sr
import pyttsx3
import os
import time
from groq import Groq
from dotenv import load_dotenv
import threading

# ---------------- INIT ---------------- #

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama-3.1-8b-instant"

client = Groq(api_key=API_KEY)

engine = pyttsx3.init()
engine.setProperty('rate', 160)

# Global flag to stop speech
if "stop_speaking" not in st.session_state:
    st.session_state.stop_speaking = False

# ---------------- FUNCTIONS ---------------- #

# 🎤 Speech to Text
def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        return recognizer.recognize_google(audio)

    except Exception as e:
        return f"Voice Error: {str(e)}"


# 🔊 Controlled Speech Function
def speak_with_stop(text):
    st.session_state.stop_speaking = False

    words = text.split()
    for word in words:
        if st.session_state.stop_speaking:
            engine.stop()
            break

        engine.say(word)
        engine.runAndWait()


# 🤖 Groq Response
def get_response(prompt):
    try:
        res = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return res.choices[0].message.content

    except Exception as e:
        return f"Groq Error: {str(e)}"


# ---------------- UI ---------------- #

st.title("🎙️ AI Voice Assistant")

# Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input
col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_input("💬 Type message")

with col2:
    if st.button("🎤 Speak"):
        user_input = listen()
        st.write("You:", user_input)

# Buttons
col1, col2 = st.columns(2)

send_clicked = col1.button("Send")
stop_clicked = col2.button("🛑 Stop Speaking")

# Stop button logic
if stop_clicked:
    st.session_state.stop_speaking = True
    engine.stop()

# Response handling
if send_clicked and user_input:
    response = get_response(user_input)
    st.session_state.chat.append((user_input, response))

    # --- Streaming text display ---
    placeholder = st.empty()
    displayed_text = ""

    for char in response:
        displayed_text += char
        placeholder.markdown(f"**🤖 Assistant:** {displayed_text}")
        time.sleep(0.01)

    # --- Speak in thread (so UI doesn't freeze) ---
    thread = threading.Thread(target=speak_with_stop, args=(response,))
    thread.start()

# Chat history
st.subheader("💬 Conversation")

for q, r in st.session_state.chat:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Assistant:** {r}")