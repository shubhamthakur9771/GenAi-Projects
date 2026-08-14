import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# ---------------- TITLE ---------------- #

st.title("🎬 Movie Information Extractor")

# ---------------- LOAD MODEL ---------------- #

model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.2
)

# ---------------- PYDANTIC MODEL ---------------- #

class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: Optional[List[str]] = []
    director: Optional[str] = None
    cast: Optional[List[str]] = []
    rating: Optional[float] = None
    summary: str

# ---------------- OUTPUT PARSER ---------------- #

parser = PydanticOutputParser(
    pydantic_object=Movie
)

# ---------------- PROMPT TEMPLATE ---------------- #

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert movie information extractor.

Extract movie information from the given paragraph.

IMPORTANT RULES:
- Return ONLY valid JSON.
- Do not add comments.
- Do not add explanation text.
- Do not use markdown.
- If information is missing, use null.
- Follow the exact format instructions.

{format_instructions}
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])

# ---------------- TEXT AREA ---------------- #

paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=250
)

# ---------------- BUTTON ---------------- #

if st.button("Extract Information"):

    if paragraph.strip() == "":
        st.warning("Please enter a paragraph.")

    else:

        try:

            # ---------------- FORMAT PROMPT ---------------- #

            final_prompt = prompt.format_messages(
                paragraph=paragraph,
                format_instructions=parser.get_format_instructions()
            )

            # ---------------- MODEL RESPONSE ---------------- #

            response = model.invoke(final_prompt)

            # ---------------- PARSE OUTPUT ---------------- #

            movie_data = parser.parse(
                response.content
            )

            # ---------------- DISPLAY OUTPUT ---------------- #

            st.subheader("Extracted Information")

            st.write(f"### 🎬 Title")
            st.write(movie_data.title)

            st.write(f"### 📅 Release Year")
            st.write(movie_data.release_year)

            st.write(f"### 🎭 Genre")
            st.write(", ".join(movie_data.genre or []))

            st.write(f"### 🎬 Director")
            st.write(movie_data.director)

            st.write(f"### 👨‍🎤 Cast")
            st.write(", ".join(movie_data.cast or []))

            st.write(f"### ⭐ Rating")
            st.write(movie_data.rating)

            st.write(f"### 📝 Summary")
            st.write(movie_data.summary)

        except Exception as e:

            st.error(f"Error: {e}")