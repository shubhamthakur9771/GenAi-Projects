import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Information Extractor",
    page_icon="🤖",
    layout="centered"
)

# ---------------- TITLE ---------------- #

st.title("🤖 Information Extraction AI")

# ---------------- LOAD MODEL ---------------- #

model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.7
)

# ---------------- SYSTEM PROMPT ---------------- #

system_prompt = """
You are an intelligent information extraction assistant.

Your job is to analyze paragraphs and extract all useful and meaningful information in a clean and organized format.

You should identify:
- Title or content name
- Genre
- Main characters
- Supporting characters
- Villains or antagonists
- Important locations
- Organizations or groups
- Important objects, weapons, or technologies
- Major events
- Powers or special abilities
- Themes and emotions
- Conflict and resolution
- Relationships between characters
- Timeline or setting
- Target audience
- Any other meaningful insights

Also generate:
- A short and crisp summary

Rules:
- Keep the output clean and readable.
- Use headings and bullet points.
- Be concise but informative.
- Infer information only if it is highly obvious.
- Avoid hallucinating unnecessary details.
"""

# ---------------- HUMAN PROMPT ---------------- #

human_prompt = """
Analyze the following paragraph and extract useful information.

Paragraph:
{paragraph}
"""

# ---------------- PROMPT TEMPLATE ---------------- #

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", human_prompt)
])

# ---------------- TEXT INPUT ---------------- #

text = st.text_area(
    "Enter Paragraph",
    height=250
)

# ---------------- BUTTON ---------------- #

if st.button("Extract Information"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    
    else:

        # Format prompt
        formatted_prompt = prompt_template.format_messages(
            paragraph=text
        )

        # Generate response
        response = model.invoke(formatted_prompt)

        # Output
        st.subheader("Extracted Information")

        st.write(response.content)