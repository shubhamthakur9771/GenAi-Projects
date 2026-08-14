import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- TITLE ---------------- #
st.title("🤖 AI Chatbot")

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("Settings")

mood = st.sidebar.selectbox(
    "Select Bot Mood",
    ["Funny", "Angry", "Happy", "Sad"]
)

# ---------------- SYSTEM PROMPT ---------------- #
system_prompts = {
    "Funny": "You are a funny AI agent. Reply in a humorous way.",
    
    "Angry": "You are an angry AI agent. Reply in an angry and irritated tone.",
    
    "Happy": "You are a very happy AI agent. Reply cheerfully and positively.",
    
    "Sad": "You are a sad AI agent. Reply in a sad and emotional tone."
}

# ---------------- LOAD MODEL ---------------- #
model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.9
)

# ---------------- SESSION STATE ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_mood" not in st.session_state:
    st.session_state.current_mood = mood

# Reset chat when mood changes
if st.session_state.current_mood != mood:

    st.session_state.current_mood = mood

    st.session_state.messages = []

    st.session_state.chat_history = []

# Add system message if empty
if len(st.session_state.messages) == 0:
    st.session_state.messages.append(
        SystemMessage(content=system_prompts[mood])
    )

# ---------------- DISPLAY CHAT ---------------- #
for role, message in st.session_state.chat_history:

    with st.chat_message(role):
        st.markdown(message)

# ---------------- USER INPUT ---------------- #
prompt = st.chat_input("Type your message here...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.chat_history.append(
        ("user", prompt)
    )

    # Add human message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Generate response
    response = model.invoke(
        st.session_state.messages
    )

    # Add AI message
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)

    st.session_state.chat_history.append(
        ("assistant", response.content)
    )